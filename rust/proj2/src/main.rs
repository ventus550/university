mod parser;
mod interpreter;
mod svg;

use parser::parse_program;
use interpreter::Turtle;
use svg::save_to_svg;
use std::fs;

fn main() {
    let file_content = fs::read_to_string("program.logo").expect("Cannot read file");
    let (_, commands) = parse_program(&file_content).expect("Failed to parse program");

    let mut turtle = Turtle::new();
    turtle.execute(commands);

    save_to_svg(&turtle, "output.svg");
}
