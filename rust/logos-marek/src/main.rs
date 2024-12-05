use std::collections::HashMap;
use std::env;
use std::fs;

use crate::effects::effects::*;
use crate::turtle::turtle::*;
use crate::run::run::*;

extern crate lalrpop;

pub mod ast;
pub mod effects;
pub mod turtle;
pub mod run;

#[macro_use]
extern crate lalrpop_util;

lalrpop_mod!(pub parser);

fn interpret_to_file(logo: &str, file_name: &str, size: u32) -> Result<(), String> {
    let logo = parser::LogoParser::new().parse(logo)
        .map_err(|e| format!("Parse error {:?}", e))?;

    let mut turtle = Turtle::new();

    let effects = run_instructions(
        logo.instructions,
        &mut HashMap::new(),
        &mut turtle,
        &logo.functions.into_iter()
            .map(|f| (f.name.clone(), f))
            .collect()
    )?;

    save_as_svg(file_name, effects, size as i32)
        .map_err(|e| format!("Saving error {:?}", e))
}

fn main() -> Result<(), String> {
    let file = env::args().nth(1).expect("Provide input file name");
    let input = fs::read_to_string(&file).expect("Unable to read input file");
    interpret_to_file(&input, &(file + ".svg"), 1000)
}
