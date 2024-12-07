use anyhow::{bail, Result};
use rand::prelude::*;

use std::collections::HashMap;

use crate::{
    canvas::{Canvas, RGB},
    eval::{Environment, EvaluatedValue, FALSE},
};

pub type ArityMap = HashMap<String, usize>;
pub struct Function(
    pub  Box<
        dyn Fn(
            Vec<EvaluatedValue>,
            &mut Canvas,
            &Functions,
            &Environment,
        ) -> Result<EvaluatedValue>,
    >,
);
pub type Functions = HashMap<String, Function>;

pub fn stdlib_arity() -> ArityMap {
    let mut map = ArityMap::new();
    map.insert("sum".to_string(), 2);
    map.insert("difference".to_string(), 2);
    map.insert("product".to_string(), 2);
    map.insert("quotient".to_string(), 2);
    map.insert("random".to_string(), 1);
    map.insert("pick".to_string(), 1);
    map.insert("clearscreen".to_string(), 0);
    map.insert("pu".to_string(), 0);
    map.insert("penup".to_string(), 0);
    map.insert("pd".to_string(), 0);
    map.insert("pendown".to_string(), 0);
    map.insert("hideturtle".to_string(), 0);
    map.insert("showturtle".to_string(), 0);
    map.insert("window".to_string(), 0);
    map.insert("fence".to_string(), 0);
    map.insert("fd".to_string(), 1);
    map.insert("forward".to_string(), 1);
    map.insert("bk".to_string(), 1);
    map.insert("back".to_string(), 1);
    map.insert("rt".to_string(), 1);
    map.insert("right".to_string(), 1);
    map.insert("lt".to_string(), 1);
    map.insert("left".to_string(), 1);
    map.insert("setcolor".to_string(), 1);
    map.insert("wait".to_string(), 1);
    map.insert("less?".to_string(), 2);
    map.insert("lessequal?".to_string(), 2);
    map.insert("greater?".to_string(), 2);
    map.insert("greaterequal?".to_string(), 2);
    map.insert("equal?".to_string(), 2);
    map.insert("notequal?".to_string(), 2);
    map.insert("stop".to_string(), 0);
    map.insert("red".to_string(), 0);
    map.insert("orange".to_string(), 0);
    map.insert("yellow".to_string(), 0);
    map.insert("green".to_string(), 0);
    map.insert("blue".to_string(), 0);
    map.insert("violet".to_string(), 0);
    map.insert("setlabelheight".to_string(), 1);
    map.insert("label".to_string(), 1);
    map.insert("repcount".to_string(), 0);
    map
}

pub fn stdlib_functions() -> Functions {
    let mut map = Functions::new();
    map.insert("sum".to_string(), arith('+'));
    map.insert("difference".to_string(), arith('-'));
    map.insert("product".to_string(), arith('*'));
    map.insert("quotient".to_string(), arith('/'));
    map.insert("random".to_string(), random());
    map.insert("pick".to_string(), pick());
    map.insert("clearscreen".to_string(), turtle_ctl('c'));
    map.insert("pu".to_string(), turtle_ctl('u'));
    map.insert("penup".to_string(), turtle_ctl('u'));
    map.insert("pd".to_string(), turtle_ctl('d'));
    map.insert("pendown".to_string(), turtle_ctl('d'));
    map.insert("hideturtle".to_string(), noop());
    map.insert("showturtle".to_string(), noop());
    map.insert("window".to_string(), noop());
    // FIXME: Some programs may rely on fence for flow control.
    map.insert("fence".to_string(), noop());
    map.insert("fd".to_string(), turtle_move('f'));
    map.insert("forward".to_string(), turtle_move('f'));
    map.insert("bk".to_string(), turtle_move('b'));
    map.insert("back".to_string(), turtle_move('b'));
    map.insert("rt".to_string(), turtle_move('r'));
    map.insert("right".to_string(), turtle_move('r'));
    map.insert("lt".to_string(), turtle_move('l'));
    map.insert("left".to_string(), turtle_move('l'));
    map.insert("setcolor".to_string(), set_color());
    map.insert("wait".to_string(), noop());
    map.insert("less?".to_string(), cmp('<'));
    map.insert("lessequal?".to_string(), cmp('≤'));
    map.insert("greater?".to_string(), cmp('>'));
    map.insert("greaterequal?".to_string(), cmp('≥'));
    map.insert("equal?".to_string(), cmp('='));
    map.insert("notequal?".to_string(), cmp('≠'));
    map.insert("stop".to_string(), stop());
    map.insert("red".to_string(), color(255, 0, 0));
    map.insert("orange".to_string(), color(255, 165, 0));
    map.insert("yellow".to_string(), color(255, 255, 0));
    map.insert("green".to_string(), color(0, 255, 0));
    map.insert("blue".to_string(), color(0, 0, 255));
    map.insert("violet".to_string(), color(238, 130, 238));
    map.insert("setlabelheight".to_string(), set_label_height());
    map.insert("label".to_string(), turtle_label());
    map.insert("repcount".to_string(), repcount());
    map
}

fn noop() -> Function {
    Function(Box::new(move |_args, _canvas, _functions, _env| Ok(FALSE)))
}

fn stop() -> Function {
    Function(Box::new(move |_args, _canvas, _functions, _env| {
        Ok(EvaluatedValue::Return)
    }))
}

fn color(r: u8, g: u8, b: u8) -> Function {
    Function(Box::new(move |_args, _canvas, _functions, _env| {
        Ok(EvaluatedValue::Color(RGB { r, g, b }))
    }))
}

fn repcount() -> Function {
    Function(Box::new(move |_args, _canvas, _functions, env| {
        if !env.contains_key("repcount") {
            bail!("Not in repeat loop");
        }
        Ok(env["repcount"].clone())
    }))
}

fn arith(op: char) -> Function {
    Function(Box::new(move |args, _canvas, _functions, _env| {
        match (&args[0], &args[1]) {
            (EvaluatedValue::Num(a), EvaluatedValue::Num(b)) => Ok(EvaluatedValue::Num(match op {
                '+' => a + b,
                '-' => a - b,
                '*' => a * b,
                '/' => a / b,
                _ => unreachable!(),
            })),
            _ => bail!("Not an integer"),
        }
    }))
}

fn cmp(op: char) -> Function {
    Function(Box::new(move |args, _canvas, _functions, _env| {
        match (&args[0], &args[1]) {
            (EvaluatedValue::Num(a), EvaluatedValue::Num(b)) => Ok(EvaluatedValue::Num(
                if match op {
                    '<' => a < b,
                    '≤' => a <= b,
                    '>' => a > b,
                    '≥' => a >= b,
                    '=' => a == b,
                    '≠' => a != b,
                    _ => unreachable!(),
                } {
                    1.
                } else {
                    0.
                },
            )),
            _ => bail!("Not an integer"),
        }
    }))
}

fn pick() -> Function {
    Function(Box::new(
        move |args, _canvas, _functions, _env| match &args[0] {
            EvaluatedValue::Array(v) => {
                let mut rng = rand::thread_rng();
                match v.iter().choose(&mut rng) {
                    Some(v) => Ok(v.clone()),
                    None => bail!("Empty array"),
                }
            }
            _ => bail!("Not an array"),
        },
    ))
}

fn random() -> Function {
    Function(Box::new(
        move |args, _canvas, _functions, _env| match &args[0] {
            EvaluatedValue::Num(max) => {
                let mut rng = rand::thread_rng();
                Ok(EvaluatedValue::Num(rng.gen_range(0.0..*max)))
            }
            _ => bail!("Not a number"),
        },
    ))
}

fn turtle_ctl(op: char) -> Function {
    Function(Box::new(move |_args, canvas, _functions, _env| {
        match op {
            'c' => canvas.clear(),
            'd' => canvas.set_pen_down(true),
            'u' => canvas.set_pen_down(false),
            _ => unreachable!(),
        }
        Ok(FALSE)
    }))
}

fn turtle_move(op: char) -> Function {
    Function(Box::new(move |args, canvas, _functions, _env| {
        match &args[0] {
            EvaluatedValue::Num(x) => match op {
                'r' => canvas.turn(*x),
                'l' => canvas.turn(-*x),
                'f' => canvas.mv(*x),
                'b' => canvas.mv(-*x),
                _ => unreachable!(),
            },
            _ => bail!("Not an integer"),
        }
        Ok(FALSE)
    }))
}

fn turtle_label() -> Function {
    Function(Box::new(move |args, canvas, _functions, _env| {
        match &args[0] {
            EvaluatedValue::String(s) => canvas.add_text(&s[1..]),
            _ => bail!("Not an integer"),
        }
        Ok(FALSE)
    }))
}

fn set_color() -> Function {
    Function(Box::new(
        move |args, canvas, _functions, _env| match &args[0] {
            EvaluatedValue::Color(c) => {
                canvas.set_color(*c);
                Ok(FALSE)
            }
            _ => bail!("Not a color"),
        },
    ))
}

fn set_label_height() -> Function {
    Function(Box::new(
        move |args, canvas, _functions, _env| match &args[0] {
            EvaluatedValue::Num(h) => {
                canvas.set_label_height(*h);
                Ok(FALSE)
            }
            _ => bail!("Not a number"),
        },
    ))
}
