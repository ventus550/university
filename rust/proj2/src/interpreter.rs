use crate::parser::Command;

#[derive(Debug)]
pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    pen_down: bool,
    pub paths: Vec<(f64, f64, f64, f64)>, // Linie w formacie (x1, y1, x2, y2)
}

impl Turtle {
    pub fn new() -> Self {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            pen_down: true,
            paths: vec![],
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
                Command::Write(text) => println!("Writing: {}", text), // Obsługa napisów
            }
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
