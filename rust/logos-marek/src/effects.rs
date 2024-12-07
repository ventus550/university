use svg::Document;
use svg::node::element::{Line, Text};
use svg::node::Text as SvgText;
use std::fs::File;
use std::io::Write;
use std::path::Path;
use crate::Pixel;

pub mod effects {
    use super::*;
    use std::f64::consts::FRAC_PI_2;

    #[derive(Debug, Clone, PartialEq)]
    pub enum Effect {
        Line(f64, f64, f64, f64, Pixel), // x1 y1 x2 y2 color
        Text(String, f64, f64, u32, f64, Pixel), // text x y size rotate color
        Cls,
        Wait(f64), // seconds
        Stop
    }

    fn to_svg(e: Effect) -> Option<svg::node::Node> {
        match e {
            Effect::Line(x1, y1, x2, y2, color) => Some(Line::new()
                .set("x1", x1)
                .set("y1", y1)
                .set("x2", x2)
                .set("y2", y2)
                .set("stroke", color)),
            Effect::Text(text, x, y, size, rotate, color) => Some(Text::new()
                .set("x", x)
                .set("y", y)
                .set("font-size", size)
                .set("fill", color)
                .set("transform", format!("rotate({} {} {})", rotate - FRAC_PI_2, x, y))
                .add(SvgText::new(text))),
            _ => None,
        }
    }

    pub fn effects_to_canvas(eff: Vec<Effect>) -> Vec<svg::node::Node> {
        eff.into_iter().rev()
            .take_while(|x| *x != Effect::Cls)
            .rev()
            .filter_map(|x| to_svg(x))
            .collect()
    }

    pub fn save_as_svg<P: AsRef<Path>>(path: P, eff: Vec<Effect>, size: i32) -> std::io::Result<()> {
        let document = Document::new()
            .set("viewBox", (-size / 2, -size / 2, size, size))
            .add(effects_to_canvas(eff));

        let mut file = File::create(path)?;
        file.write_all(document.to_string().as_bytes())?;
        Ok(())
    }
}
