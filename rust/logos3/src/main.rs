use std::collections::HashMap;

#[derive(Clone, Debug)]
struct Turtle {
    x: f64,
    y: f64,
    angle: f64, // In degrees
}

impl Turtle {
    fn new() -> Self {
        Turtle {
            x: 0.0,
            y: 0.0,
            angle: 0.0,
        }
    }

    fn forward(&mut self, distance: f64) {
        let rad = self.angle.to_radians();
        self.x += rad.cos() * distance;
        self.y += rad.sin() * distance;
        println!("DRAW LINE TO ({:.2}, {:.2})", self.x, self.y); // Simulate drawing
    }

    fn back(&mut self, distance: f64) {
        self.forward(-distance);
    }

    fn left(&mut self, degrees: f64) {
        self.angle -= degrees;
    }

    fn right(&mut self, degrees: f64) {
        self.angle += degrees;
    }

    fn reset(&mut self) {
        self.x = 0.0;
        self.y = 0.0;
        self.angle = 0.0;
        println!("SCREEN CLEARED");
    }
}

type Env = HashMap<String, Vec<String>>;

fn interpret_line(turtle: &mut Turtle, env: &Env, tokens: &[String], mut vars: HashMap<String, f64>) {
    if tokens.is_empty() {
        return;
    }

    let cmd = tokens[0].as_str();
    match cmd {
        "forward" => {
            let dist = evaluate_expression(&tokens[1], &vars);
            turtle.forward(dist);
        }
        "back" => {
            let dist = evaluate_expression(&tokens[1], &vars);
            turtle.back(dist);
        }
        "left" => {
            let angle = evaluate_expression(&tokens[1], &vars);
            turtle.left(angle);
        }
        "right" => {
            let angle = evaluate_expression(&tokens[1], &vars);
            turtle.right(angle);
        }
        "clearscreen" => {
            turtle.reset();
        }
        "stop" => {
            // No-op, used for terminating a procedure early
        }
        _ if cmd.starts_with(":") => {
            // Parameter access
            let param = &cmd[1..];
            vars.insert(param.to_string(), evaluate_expression(&tokens[1], &vars));
        }
        _ if env.contains_key(cmd) => {
            // User-defined procedure call
            if tokens.len() > 1 {
                vars.insert(":size".to_string(), evaluate_expression(&tokens[1], &vars));
            }
            if let Some(body) = env.get(cmd) {
                interpret_program(turtle, env, body, vars.clone());
            }
        }
        _ => {
            eprintln!("Unknown command: {}", cmd);
        }
    }
}

fn evaluate_expression(expr: &str, vars: &HashMap<String, f64>) -> f64 {
    let expr = expr.replace(":", "");
    if let Ok(value) = expr.parse::<f64>() {
        value
    } else if let Some(&value) = vars.get(&expr) {
        value
    } else {
        eprintln!("Unknown variable or invalid expression: {}", expr);
        0.0
    }
}

fn interpret_program(turtle: &mut Turtle, env: &Env, program: &[String], vars: HashMap<String, f64>) {
    for line in program {
        let tokens: Vec<String> = line.split_whitespace().map(|s| s.to_string()).collect();
        interpret_line(turtle, env, &tokens, vars.clone());
    }
}

fn main() {
    let mut env: Env = HashMap::new();

    // Define the "tree" procedure
    env.insert(
        "tree".to_string(),
        vec![
            "if :size < 5 [stop]".to_string(),
            "forward :size/3".to_string(),
            "left 30 tree :size*2/3 right 30".to_string(),
            "forward :size/6".to_string(),
            "right 25 tree :size/2 left 25".to_string(),
            "forward :size/3".to_string(),
            "right 25 tree :size/2 left 25".to_string(),
            "forward :size/6".to_string(),
            "back :size".to_string(),
        ],
    );

    let program = vec![
        "clearscreen".to_string(),
        "tree 150".to_string(),
    ];

    let mut turtle = Turtle::new();
    interpret_program(&mut turtle, &env, &program, HashMap::new());
}
