use crate::parser::Command;
use std::collections::HashMap;

#[derive(Debug)]
pub struct Executor {
    position: (f64, f64),
    angle: f64,
    pen_down: bool,
    procedures: HashMap<String, Vec<Command>>,
    variables: HashMap<String, f64>,
    pub drawing: Vec<(f64, f64, f64, f64)>, // Lines: (x1, y1, x2, y2)
}

impl Executor {
    pub fn new() -> Self {
        Self {
            position: (0.0, 0.0),
            angle: 0.0,
            pen_down: true,
            procedures: HashMap::new(),
            variables: HashMap::new(),
            drawing: Vec::new(),
        }
    }

    pub fn execute(&mut self, commands: &[Command]) {
        for command in commands {
            match command {
                Command::Forward(distance) => self.forward(*distance),
                Command::Back(distance) => self.forward(-*distance),
                Command::Left(angle) => self.angle += angle,
                Command::Right(angle) => self.angle -= angle,
                Command::Clearscreen => self.drawing.clear(),
                Command::To(name, body) => {
                    self.procedures.insert(name.clone(), body.clone());
                }
                Command::Call(name, args) => {
                    if let Some(procedure) = self.procedures.get(name).cloned() {
                        self.execute(&procedure); // Mutable borrow happens here, after cloning
                    }
                }
                Command::Stop => break,
            }
        }
    }

    fn forward(&mut self, distance: f64) {
        let (x, y) = self.position;
        let radians = self.angle.to_radians();
        let new_x = x + distance * radians.cos();
        let new_y = y + distance * radians.sin();

        if self.pen_down {
            self.drawing.push((x, y, new_x, new_y));
        }

        self.position = (new_x, new_y);
    }
}
