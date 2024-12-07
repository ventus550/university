use anyhow::{bail, Result};

use crate::{
    canvas::{Canvas, RGB},
    parser::{Expression, Value},
    stdlib::{stdlib_functions, Function, Functions},
};

use std::collections::HashMap;

#[derive(Debug, Clone, PartialEq)]
pub enum EvaluatedValue {
    Return,
    Num(f32),
    Color(RGB),
    String(String),
    Array(Vec<EvaluatedValue>),
}

pub const FALSE: EvaluatedValue = EvaluatedValue::Num(0.);
pub type Environment = HashMap<String, EvaluatedValue>;

impl EvaluatedValue {
    fn from_value(
        value: &Value,
        canvas: &mut Canvas,
        functions: &Functions,
        env: &Environment,
    ) -> Result<Self> {
        match value {
            Value::Num(i) => Ok(Self::Num(*i)),
            Value::String(s) => Ok(Self::String(s.to_string())),
            Value::Variable(name) => {
                if !env.contains_key(name) {
                    bail!("Unknown variable {}", name);
                }
                Ok(env[name].clone())
            }
            Value::Expression(e) => eval_single(e, canvas, functions, env),
            Value::Array(arr) => Ok(Self::Array(
                arr.iter()
                    .map(|x| EvaluatedValue::from_value(x, canvas, functions, env))
                    .collect::<Result<Vec<_>>>()?,
            )),
        }
    }
}

fn eval_single(
    instruction: &Expression,
    canvas: &mut Canvas,
    functions: &Functions,
    env: &Environment,
) -> Result<EvaluatedValue> {
    match instruction {
        Expression::Call(fn_name, args) => {
            let values = args
                .iter()
                .map(|x| EvaluatedValue::from_value(x, canvas, functions, env))
                .collect::<Result<Vec<_>>>()?;
            if !functions.contains_key(fn_name) {
                bail!("Unknown function {}", fn_name);
            }
            functions[fn_name].0(values, canvas, functions, env)
        }
        Expression::FunctionDefinition(_fn_name, _args, _body) => {
            bail!("Operation not supported here")
        }
        Expression::Repeat(times, body) => {
            for i in 0..*times {
                let mut env = env.clone();
                env.insert("repcount".to_string(), EvaluatedValue::Num((i + 1) as f32));
                if let EvaluatedValue::Return = eval_many(body, canvas, functions, &env)? {
                    return Ok(EvaluatedValue::Return);
                }
            }
            Ok(FALSE)
        }
        Expression::If(cond, body) => {
            let cond = eval_single(cond, canvas, functions, env)?;
            if cond == EvaluatedValue::Return {
                return Ok(EvaluatedValue::Return);
            }
            if cond != FALSE {
                if let EvaluatedValue::Return = eval_many(body, canvas, functions, env)? {
                    return Ok(EvaluatedValue::Return);
                }
            }
            Ok(FALSE)
        }
    }
}

fn eval_many(
    instructions: &Vec<Expression>,
    canvas: &mut Canvas,
    functions: &Functions,
    env: &Environment,
) -> Result<EvaluatedValue> {
    for i in instructions {
        if let EvaluatedValue::Return = eval_single(i, canvas, functions, env)? {
            return Ok(EvaluatedValue::Return);
        }
    }
    Ok(FALSE)
}

fn wrap_fn(args: &Vec<String>, body: &Vec<Expression>) -> Function {
    let args = args.clone();
    let body = body.clone();
    Function(Box::new(move |values, canvas, functions, env| {
        let mut env = env.clone();
        env.extend(
            args.clone()
                .into_iter()
                .zip(values)
                .collect::<Environment>(),
        );
        eval_many(&body, canvas, functions, &env)?;
        // We don't return EvaluatedValue::Return from here.
        Ok(FALSE)
    }))
}

pub fn eval(instructions: &Vec<Expression>, canvas: &mut Canvas) -> Result<()> {
    let mut functions = stdlib_functions();
    let env = Environment::new();
    for i in instructions {
        match i {
            Expression::FunctionDefinition(fn_name, args, body) => {
                let fun = wrap_fn(args, body);
                functions.insert(fn_name.to_string(), fun);
            }
            _ => {
                if let EvaluatedValue::Return = eval_single(i, canvas, &functions, &env)? {
                    break;
                }
            }
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::EvaluatedValue as EV;
    use super::*;
    use crate::parser::Expression as E;
    use crate::parser::Value as V;

    #[test]
    fn test_sum() {
        let mut env = Environment::new();
        env.insert(":x".to_string(), EV::Num(2.));
        assert_eq!(
            eval_single(
                &E::Call(
                    "sum".to_string(),
                    vec![V::Num(1.), V::Variable(":x".to_string())]
                ),
                &mut Canvas::new(1, 1),
                &stdlib_functions(),
                &env
            )
            .unwrap(),
            EV::Num(3.)
        );
    }

    #[test]
    fn test_bool() {
        assert_eq!(
            eval_single(
                &E::Call("greaterequal?".to_string(), vec![V::Num(2.), V::Num(0.)]),
                &mut Canvas::new(1, 1),
                &stdlib_functions(),
                &Environment::new()
            )
            .unwrap(),
            EV::Num(1.)
        );
    }
}
