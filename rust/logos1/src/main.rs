mod parser;
mod interpreter;
mod svg;

use parser::{parse, Token};
use interpreter::Turtle;
use svg::save_as_svg;
use logos::Logos;

fn main() {
    let code = r#"
        to tree :size
           if :size < 5 [forward :size back :size stop]
           forward :size/3
           left 30 tree :size*2/3 right 30
           forward :size/6
           right 25 tree :size/2 left 25
           forward :size/3
           right 25 tree :size/2 left 25
           forward :size/6
           back :size
        end
        clearscreen
        tree 150
    "#;

    let tokens = Token::lexer(code).collect::<Vec<_>>();
    let ast = parse(&tokens);

    let mut turtle = Turtle::new();
    let mut variables = std::collections::HashMap::new();
    variables.insert(":size".to_string(), 150.0);

    turtle.execute(&ast, &mut variables);
    save_as_svg(turtle.get_path(), "output.svg");
}
