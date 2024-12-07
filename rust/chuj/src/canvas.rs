use std::{f32::consts::PI, fs::File, io::Write};

use anyhow::Result;

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct Point {
    x: f32,
    y: f32,
}

#[derive(Debug, Clone, Copy, PartialEq)]
pub struct RGB {
    pub r: u8,
    pub g: u8,
    pub b: u8,
}

#[derive(Debug, Clone, PartialEq)]
enum Shape {
    Line(Point, Point, RGB),
    Text(Point, f32, String, f32, RGB),
}

pub struct Canvas {
    width: u32,
    height: u32,
    shapes: Vec<Shape>,
    position: Point,
    direction: f32,
    pen_down: bool,
    label_height: f32,
    color: RGB,
}

impl Canvas {
    pub fn new(width: u32, height: u32) -> Self {
        Self {
            width,
            height,
            shapes: vec![],
            position: Point {
                x: width as f32 / 2.,
                y: height as f32 / 2.,
            },
            direction: 0.,
            pen_down: true,
            label_height: 1.,
            color: RGB {
                r: 0xc3,
                g: 0x97,
                b: 0x0d,
            },
        }
    }

    pub fn clear(&mut self) {
        self.shapes.clear();
    }

    pub fn set_pen_down(&mut self, pen_down: bool) {
        self.pen_down = pen_down;
    }

    pub fn turn(&mut self, deg: f32) {
        self.direction = (self.direction + deg) % 360.;
    }

    pub fn mv(&mut self, distance: f32) {
        let old_pos = self.position;
        let dir = self.direction * 2. * PI / 360.;
        self.position = Point {
            x: old_pos.x + distance * dir.sin(),
            y: old_pos.y - distance * dir.cos(),
        };
        if self.pen_down {
            self.shapes
                .push(Shape::Line(old_pos, self.position, self.color));
        }
    }

    pub fn set_color(&mut self, color: RGB) {
        self.color = color;
    }

    pub fn set_label_height(&mut self, height: f32) {
        self.label_height = height;
    }

    pub fn add_text(&mut self, text: &str) {
        self.shapes.push(Shape::Text(
            self.position,
            self.direction,
            text.to_string(),
            self.label_height,
            self.color,
        ));
    }

    pub fn render_to_svg(&self, path: &str) -> Result<()> {
        let mut file = File::create(&path).unwrap();

        file.write(
            format!(
                "<svg viewBox=\"0 0 {} {}\" xmlns=\"http://www.w3.org/2000/svg\">\n",
                self.width, self.height
            )
            .as_bytes(),
        )?;
        for shape in &self.shapes {
            match shape {
                Shape::Line(from, to, color) => {
                    file.write(
                        format!(
                            "<path d=\"M{},{} L{},{}\" fill=\"transparent\" stroke=\"rgb({},{},{})\" stroke-width=\"1\"/>\n",
                            from.x, from.y, to.x, to.y, color.r, color.g, color.b
                        )
                        .as_bytes(),
                    )?;
                }
                Shape::Text(origin, direction, text, height, color) => {
                    file.write(
                        format!(
                            "<g transform=\"translate({},{})\"><text text-anchor=\"start\" style=\"fill: rgb({},{},{}); font-size: {}px; font-family: monospace;\" transform=\"rotate({})\">{}</text></g>\n",
                            origin.x, origin.y, color.r, color.g, color.b, height, direction - 90., text
                        )
                        .as_bytes(),
                    )?;
                }
            }
        }
        file.write(b"</svg>\n")?;

        Ok(())
    }
}
