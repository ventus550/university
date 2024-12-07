use std::collections::HashMap;
use crate::parser::Command;

#[derive(Debug)]
pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    pen_down: bool,
    pub paths: Vec<(f64, f64, f64, f64)>,
    functions: HashMap<String, (Vec<String>, Vec<Command>)>, // Function definitions
    variables: HashMap<String, f64>,                        // Variable storage
}

impl Turtle {
    pub fn new() -> Self {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            pen_down: true,
            paths: vec![],
            functions: HashMap::new(),
            variables: HashMap::new(),
        }
    }

    pub fn execute(&mut self, commands: Vec<Command>) {
        for command in commands {
            match command {
                Command::Forward(dist) => self.move_turtle(dist),
                Command::Backward(dist) => self.move_turtle(-dist),
                Command::Left(angle) => self.angle -= angle,
                Command::Right(angle) => self.angle += angle,
                Command::PenUp => self.pen_down = false,
                Command::PenDown => self.pen_down = true,
                Command::SetPosition(x, y) => self.set_position(x, y),
                Command::Write(text) => println!("Writing: {}", text),
                Command::DefineFunction(name, params, body) => {
                    self.functions.insert(name, (params, body));
                }
                Command::CallFunction(name, args) => {
                    if let Some((params, body)) = self.functions.get(&name) {
                        let prev_vars = self.variables.clone();
                        for (param, arg) in params.iter().zip(args.iter()) {
                            self.variables.insert(param.clone(), *arg);
                        }
                        self.execute(body.clone());
                        self.variables = prev_vars; // Restore previous state
                    }
                }
                Command::If(condition, then_branch, else_branch) => {
                    if self.evaluate_condition(*condition) {
                        self.execute(then_branch);
                    } else {
                        self.execute(else_branch);
                    }
                }
            }
        }
    }

    fn evaluate_condition(&self, condition: Command) -> bool {
        match condition {
            Command::Forward(dist) => self.variables.get("size").unwrap_or(&0.0) < &dist,
            _ => false,
        }
    }

    fn move_turtle(&mut self, distance: f64) {
        let radians = self.angle.to_radians();
        let new_x = self.x + radians.cos() * distance;
        let new_y = self.y + radians.sin() * distance;

        if self.pen_down {
            self.paths.push((self.x, self.y, new_x, new_y));
        }

        self.x = new_x;
        self.y = new_y;
    }

    fn set_position(&mut self, x: f64, y: f64) {
        if self.pen_down {
            self.paths.push((self.x, self.y, x, y));
        }
        self.x = x;
        self.y = y;
    }
}
