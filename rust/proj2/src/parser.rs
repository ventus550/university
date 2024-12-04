use nom::{
    IResult,
    bytes::complete::tag,
    character::complete::{alpha1, digit1, multispace0, space1},
    sequence::{preceded, separated_pair},
    combinator::map,
    multi::many0,
    branch::alt,
};

// Enum dla różnych poleceń w LOGO
#[derive(Debug, Clone)]
pub enum Command {
    Forward(f64),
    Backward(f64),
    Left(f64),
    Right(f64),
    PenUp,
    PenDown,
    SetPosition(f64, f64),
    Write(String),
}

// Funkcja parsująca jedno polecenie
fn parse_command(input: &str) -> IResult<&str, Command> {
    let forward = map(preceded(tag("FORWARD "), parse_number), Command::Forward);
    let backward = map(preceded(tag("BACKWARD "), parse_number), Command::Backward);
    let left = map(preceded(tag("LEFT "), parse_number), Command::Left);
    let right = map(preceded(tag("RIGHT "), parse_number), Command::Right);
    let penup = map(tag("PENUP"), |_| Command::PenUp);
    let pendown = map(tag("PENDOWN"), |_| Command::PenDown);
    let setpos = map(
        preceded(tag("SETPOS "), separated_pair(parse_number, space1, parse_number)),
        |(x, y)| Command::SetPosition(x, y),
    );
    let write = map(preceded(tag("WRITE "), alpha1), |text: &str| {
        Command::Write(text.to_string())
    });

    alt((forward, backward, left, right, penup, pendown, setpos, write))(input)
}

// Funkcja pomocnicza do parsowania liczb
fn parse_number(input: &str) -> IResult<&str, f64> {
    map(digit1, |num: &str| num.parse::<f64>().unwrap())(input)
}

// Główny parser programu LOGO
pub fn parse_program(input: &str) -> IResult<&str, Vec<Command>> {
    many0(preceded(multispace0, parse_command))(input)
}
