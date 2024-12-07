use std::fs;

mod parser;
mod executor;
mod renderer;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: logo_interpreter <file>");
        std::process::exit(1);
    }

    let filename = &args[1];
    let code = fs::read_to_string(filename).expect("Failed to read the file");

    // Step 1: Parse the LOGO program
    let ast = parser::parse(&code).expect("Failed to parse the LOGO program");

    // Step 2: Execute the program
    let mut executor = executor::Executor::new();
    executor.execute(&ast);

    // Step 3: Render the output to SVG
    let svg = renderer::render(&executor.drawing);
    fs::write("output.svg", svg).expect("Failed to write the SVG file");

    println!("SVG output saved to output.svg");
}
