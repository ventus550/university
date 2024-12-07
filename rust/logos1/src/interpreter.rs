use crate::parser::ASTNode;

pub struct Turtle {
    x: f64,
    y: f64,
    angle: f64,
    path: Vec<(f64, f64)>,
}

impl Turtle {
    pub fn new() -> Self {
        Self {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
            path: vec![(0.0, 0.0)],
        }
    }

    pub fn execute(&mut self, ast: &[ASTNode], variables: &mut std::collections::HashMap<String, f64>) {
        for node in ast {
            match node {
                ASTNode::Command(cmd, args) => match cmd.as_str() {
                    "Clearscreen" => self.path.clear(),
                    "Forward" => {
                        if let ASTNode::Number(n) = self.evaluate(&args[0], variables) {
                            self.forward(n);
                        }
                    }
                    "Back" => {
                        if let ASTNode::Number(n) = self.evaluate(&args[0], variables) {
                            self.forward(-n);
                        }
                    }
                    "Left" => {
                        if let ASTNode::Number(n) = self.evaluate(&args[0], variables) {
                            self.left(n);
                        }
                    }
                    "Right" => {
                        if let ASTNode::Number(n) = self.evaluate(&args[0], variables) {
                            self.right(n);
                        }
                    }
                    _ => {}
                },
                _ => {}
            }
        }
    }

    fn forward(&mut self, distance: f64) {
        let rad = self.angle.to_radians();
        self.x += distance * rad.cos();
        self.y += distance * rad.sin();
        self.path.push((self.x, self.y));
    }

    fn left(&mut self, angle: f64) {
        self.angle -= angle;
    }

    fn right(&mut self, angle: f64) {
        self.angle += angle;
    }

    fn evaluate(&self, node: &ASTNode, variables: &std::collections::HashMap<String, f64>) -> ASTNode {
        match node {
            ASTNode::Number(n) => ASTNode::Number(*n),
            ASTNode::Variable(v) => {
                if let Some(&value) = variables.get(v) {
                    ASTNode::Number(value)
                } else {
                    ASTNode::Number(0.0)
                }
            }
            _ => node.clone(),
        }
    }

    pub fn get_path(&self) -> &[(f64, f64)] {
        &self.path
    }
}
