use logos::Logos;

#[derive(Logos, Debug, PartialEq)]
pub enum Token {
    #[token("to")]
    FunctionStart,
    #[token("end")]
    FunctionEnd,

    #[token("[")]
    BlockStart,
    #[token("]")]
    BlockEnd,

    #[token("(")]
    ExpressionStart,
    #[token(")")]
    ExpressionEnd,

    #[regex(":[a-zA-Z0-9?]+")]
    Variable,

    #[regex("[0-9-.]+", |lex| lex.slice().parse())]
    Num(f32),
    #[regex("'[a-zA-Z0-9]+")]
    #[regex("\"[a-zA-Z0-9]+")]
    String,
    #[regex("[a-zA-Z][a-zA-Z0-9?]+")]
    Text,

    #[error]
    #[regex("[ \\t\\r\\n]+", logos::skip)]
    Error,
}
