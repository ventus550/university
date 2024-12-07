use canvas::Canvas;
use eval::eval;
use parser::parse;

mod canvas;
mod eval;
mod lexer;
mod parser;
mod stdlib;

fn main() {
    let file = std::env::args().nth(1).expect("Provide input file name");
    let input = std::fs::read_to_string(file.clone()).expect("Unable to read input file");
    let parsed = parse(&input).expect("Unable to parse");
    println!("Parsed!");
 
    let mut canvas = Canvas::new(1000, 1000);
    eval(&parsed, &mut canvas).expect("Evaluation failed");
    println!("Evaluated!");

    let output = file + ".svg";
    canvas
        .render_to_svg(&output)
        .expect("Failed to write output");
    println!("Saved!");
}
