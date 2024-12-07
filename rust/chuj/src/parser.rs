use anyhow::{bail, Result};
use logos::{Lexer, Logos};

use crate::lexer::Token;
use crate::stdlib::{stdlib_arity, ArityMap};

// Differences:
// - when defining a function, arity is needed
// - no infix operators

#[derive(Debug, Clone, PartialEq)]
pub enum Value {
    Num(f32),
    String(String),
    Variable(String),
    Expression(Expression),
    Array(Vec<Value>),
}

#[derive(Debug, Clone, PartialEq)]
pub enum Expression {
    Call(String, Vec<Value>),
    FunctionDefinition(String, Vec<String>, Vec<Expression>),
    Repeat(usize, Vec<Expression>),
    If(Box<Expression>, Vec<Expression>),
}

fn parse_array(lexer: &mut Lexer<Token>, known_fn: &mut ArityMap) -> Result<Value> {
    let mut acc = vec![];
    while let Some(tt) = lexer.next() {
        match tt {
            Token::BlockStart => acc.push(parse_array(lexer, known_fn)?),
            Token::BlockEnd => return Ok(Value::Array(acc)),
            Token::ExpressionStart => {
                acc.push(Value::Expression(parse_expression(lexer, known_fn)?))
            }
            Token::Variable => acc.push(Value::Variable(lexer.slice().to_string())),
            Token::Num(i) => acc.push(Value::Num(i)),
            Token::String => acc.push(Value::String(lexer.slice().to_string())),
            Token::Text => acc.push(Value::Expression(parse_call(
                lexer.slice(),
                lexer,
                known_fn,
            )?)),
            _ => bail!("Unexpected token {}", lexer.slice()),
        }
    }
    bail!("Unexpected end of array");
}

fn is_special_form(name: &str) -> bool {
    name == "if" || name == "repeat"
}

fn parse_special_form(
    form_name: &str,
    lexer: &mut Lexer<Token>,
    known_fn: &mut ArityMap,
) -> Result<Expression> {
    if form_name == "if" {
        let fn_name = if let Some(Token::Text) = lexer.next() {
            lexer.slice()
        } else {
            bail!("Missing function name");
        };

        let cond = Box::new(parse_call(fn_name, lexer, known_fn)?);

        if let Some(Token::BlockStart) = lexer.next() {
        } else {
            bail!("Missing '['");
        }
        let body = parse_block(lexer, Some(Token::BlockEnd), known_fn)?;

        return Ok(Expression::If(cond, body));
    }
    if form_name == "repeat" {
        let times = if let Some(Token::Num(i)) = lexer.next() {
            i as usize
        } else {
            bail!("Missing number of times to repeat");
        };

        if let Some(Token::BlockStart) = lexer.next() {
        } else {
            bail!("Missing '['");
        }
        let body = parse_block(lexer, Some(Token::BlockEnd), known_fn)?;

        return Ok(Expression::Repeat(times, body));
    }
    bail!("Unknown special form");
}

fn parse_call(
    fn_name: &str,
    lexer: &mut Lexer<Token>,
    known_fn: &mut ArityMap,
) -> Result<Expression> {
    if is_special_form(fn_name) {
        return parse_special_form(fn_name, lexer, known_fn);
    }
    if !known_fn.contains_key(fn_name) {
        bail!("Unknown function {}", fn_name);
    }
    let arity = known_fn[fn_name];
    let mut acc = vec![];
    while acc.len() != arity {
        if let Some(tt) = lexer.next() {
            match tt {
                Token::BlockStart => acc.push(parse_array(lexer, known_fn)?),
                Token::ExpressionStart => {
                    acc.push(Value::Expression(parse_expression(lexer, known_fn)?))
                }
                Token::Variable => acc.push(Value::Variable(lexer.slice().to_string())),
                Token::Num(i) => acc.push(Value::Num(i)),
                Token::String => acc.push(Value::String(lexer.slice().to_string())),
                _ => bail!("Unexpected token {}", lexer.slice()),
            }
        } else {
            bail!("Not enough arguments");
        }
    }
    Ok(Expression::Call(fn_name.to_string(), acc))
}

fn parse_expression(lexer: &mut Lexer<Token>, known_fn: &mut ArityMap) -> Result<Expression> {
    if let Some(tt) = lexer.next() {
        let expr = match tt {
            Token::Text => parse_call(lexer.slice(), lexer, known_fn)?,
            _ => bail!("Unexpected token {}", lexer.slice()),
        };
        if let Some(Token::ExpressionEnd) = lexer.next() {
            return Ok(expr);
        } else {
            bail!("Missing ')'");
        }
    } else {
        bail!("Missing function name");
    }
}

fn parse_function(lexer: &mut Lexer<Token>, known_fn: &mut ArityMap) -> Result<Expression> {
    let fn_name = if let Some(tt) = lexer.next() {
        match tt {
            Token::Text => lexer.slice(),
            _ => bail!("Unexpected token {}", lexer.slice()),
        }
    } else {
        bail!("Missing function name");
    };

    let arity = if let Some(tt) = lexer.next() {
        match tt {
            Token::Num(i) => i as usize,
            _ => bail!("Unexpected token {}", lexer.slice()),
        }
    } else {
        bail!("Missing arity");
    };

    known_fn.insert(fn_name.to_string(), arity);

    let mut args = vec![];
    while args.len() < arity {
        if let Some(tt) = lexer.next() {
            match tt {
                Token::Variable => args.push(lexer.slice().to_string()),
                _ => bail!("Too few variables in function definition"),
            }
        }
    }
    let body = parse_block(lexer, Some(Token::FunctionEnd), known_fn)?;

    Ok(Expression::FunctionDefinition(
        fn_name.to_string(),
        args,
        body,
    ))
}

fn parse_block(
    lexer: &mut Lexer<Token>,
    expected_close: Option<Token>,
    known_fn: &mut ArityMap,
) -> Result<Vec<Expression>> {
    let mut acc = vec![];
    while let Some(tt) = lexer.next() {
        match tt {
            Token::FunctionStart => acc.push(parse_function(lexer, known_fn)?),
            Token::ExpressionStart => acc.push(parse_expression(lexer, known_fn)?),
            Token::Text => acc.push(parse_call(lexer.slice(), lexer, known_fn)?),
            _ if Some(tt) == expected_close => return Ok(acc),
            _ => bail!("Unexpected token {}", lexer.slice()),
        }
    }
    if !expected_close.is_none() {
        bail!("Unclosed bracket");
    }
    Ok(acc)
}

pub fn parse(program: &str) -> Result<Vec<Expression>> {
    let mut lex = Token::lexer(program);
    let mut known_fn = stdlib_arity();
    parse_block(&mut lex, None, &mut known_fn)
}

