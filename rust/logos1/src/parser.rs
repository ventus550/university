use logos::Logos;

#[derive(Logos, Debug, PartialEq, Clone)]
pub enum Token {
    #[token("to")]
    To,
    #[token("end")]
    End,
    #[token("if")]
    If,
    #[token("forward")]
    Forward,
    #[token("back")]
    Back,
    #[token("left")]
    Left,
    #[token("right")]
    Right,
    #[token("stop")]
    Stop,
    #[token("clearscreen")]
    Clearscreen,
    #[regex(r"[-+]?\d*\.?\d+", |lex| lex.slice().parse())]
    Number(f64),
    #[regex(r":[a-zA-Z_][a-zA-Z0-9_]*", |lex| lex.slice().to_string())]
    Variable(String),
    #[regex(r"[a-zA-Z_][a-zA-Z0-9_]*", |lex| lex.slice().to_string())]
    Word(String),
    #[error]
    #[regex(r"[ \t\n\f]+", logos::skip)]
    Error,
}

#[derive(Debug, Clone)]
pub enum ASTNode {
    Command(String, Vec<ASTNode>),
    Number(f64),
    Variable(String),
    Block(Vec<ASTNode>),
}

pub fn parse(tokens: &[Token]) -> Vec<ASTNode> {
    let mut nodes = Vec::new();
    let mut i = 0;

    while i < tokens.len() {
        match &tokens[i] {
            Token::To => {
                i += 1;
                if let Token::Word(name) = &tokens[i] {
                    i += 1;
                    let mut body = Vec::new();
                    while tokens[i] != Token::End {
                        body.push(parse_command(tokens, &mut i));
                    }
                    i += 1; // Skip "end"
                    nodes.push(ASTNode::Command(name.clone(), vec![ASTNode::Block(body)]));
                }
            }
            _ => nodes.push(parse_command(tokens, &mut i)),
        }
    }

    nodes
}

fn parse_command(tokens: &[Token], i: &mut usize) -> ASTNode {
    match &tokens[*i] {
        Token::Forward | Token::Back | Token::Left | Token::Right => {
            let command = tokens[*i].clone();
            *i += 1;
            let arg = parse_expression(tokens, i);
            ASTNode::Command(format!("{:?}", command), vec![arg])
        }
        Token::If => {
            *i += 1;
            let condition = parse_expression(tokens, i);
            let mut body = Vec::new();
            while tokens[*i] != Token::Stop {
                body.push(parse_command(tokens, i));
            }
            *i += 1; // Skip "stop"
            ASTNode::Command("If".to_string(), vec![condition, ASTNode::Block(body)])
        }
        Token::Clearscreen => {
            *i += 1;
            ASTNode::Command("Clearscreen".to_string(), vec![])
        }
        _ => {
            *i += 1;
            ASTNode::Number(0.0) // Default placeholder
        }
    }
}

fn parse_expression(tokens: &[Token], i: &mut usize) -> ASTNode {
    match &tokens[*i] {
        Token::Number(n) => {
            *i += 1;
            ASTNode::Number(*n)
        }
        Token::Variable(v) => {
            *i += 1;
            ASTNode::Variable(v.clone())
        }
        _ => panic!("Unexpected token {:?}", tokens[*i]),
    }
}
