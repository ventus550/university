use nom::{
    branch::alt,
    bytes::complete::{tag, take_while},
    character::complete::{digit1, space0, space1},
    combinator::map,
    multi::many0,
    sequence::{preceded, tuple},
    IResult,
};

#[derive(Debug, Clone)]
pub enum Command {
    Forward(f64),
    Back(f64),
    Left(f64),
    Right(f64),
    Clearscreen,
    To(String, Vec<Command>),
    Call(String, Vec<f64>),
    Stop,
}

pub fn parse(input: &str) -> Result<Vec<Command>, String> {
    match program(input) {
        Ok((_, cmds)) => Ok(cmds),
        Err(_) => Err("Failed to parse input".to_string()),
    }
}

fn program(input: &str) -> IResult<&str, Vec<Command>> {
    many0(preceded(space0, command))(input)
}

fn command(input: &str) -> IResult<&str, Command> {
    alt((
        map(preceded(tag("forward "), expr), Command::Forward),
        map(preceded(tag("back "), expr), Command::Back),
        map(preceded(tag("left "), expr), Command::Left),
        map(preceded(tag("right "), expr), Command::Right),
        map(tag("clearscreen"), |_| Command::Clearscreen),
        map(tag("stop"), |_| Command::Stop),
        to_command,
        call_command,
    ))(input)
}

fn to_command(input: &str) -> IResult<&str, Command> {
    let (input, (_, name, _, body, _)) = tuple((
        tag("to "),
        identifier,
        space1,
        many0(command),
        tag("end"),
    ))(input)?;
    Ok((input, Command::To(name, body)))
}

fn call_command(input: &str) -> IResult<&str, Command> {
    let (input, (name, args)) = tuple((
        identifier,
        many0(preceded(space1, expr)),
    ))(input)?;
    Ok((input, Command::Call(name, args)))
}

fn expr(input: &str) -> IResult<&str, f64> {
    map(digit1, |s: &str| s.parse().unwrap())(input)
}

fn identifier(input: &str) -> IResult<&str, String> {
    map(take_while(|c: char| c.is_alphanumeric()), |s: &str| s.to_string())(input)
}
