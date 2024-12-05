
use std::collections::HashMap;

use crate::ast::ast::*;
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

fn create_functions_map(func: Vec<FuncDeclaration>) -> HashMap<String, FuncDeclaration> {
    let mut res = HashMap::new();
    for f in func {
        res.insert(f.name.clone(), f);
    }
    res
}

fn interprate_to_file(logo: &str, file_name: &str, size: u32) -> Result<(), String> {
    let logo : Logo = match parser::LogoParser::new().parse(logo) {
        Ok(l) => l,
        Err(e) => return Err(format!("Parse error {:?}", e))
    };

    let mut turtle = Turtle::new();

    let effects = run_instructions(logo.instructions, &mut HashMap::new(), &mut turtle, 
        &create_functions_map(logo.functions))?;

    match save_as_svg(file_name, effects, size as i32) {
        Ok(()) => Ok(()),
        Err(e) => Err(format!("Saving error {:?}", e))
    }
}

fn main() -> Result<(), String>{
    let file = std::env::args().nth(1).expect("Provide input file name");
    let input = std::fs::read_to_string(file.clone()).expect("Unable to read input file");
    let output = file + ".svg";
    interprate_to_file(&input, &output, 1000)?;
    Ok(())
}
