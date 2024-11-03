use std::fs::File;
use std::io::{self, Write};

pub struct Image {
    width: usize,
    height: usize,
    pixels: Vec<u8>,
}

impl Image {
    pub fn new(width: usize, height: usize) -> Self {
        Image {
            width,
            height,
            pixels: vec![0; width * height * 3],
        }
    }

    pub fn set_pixel(&mut self, x: usize, y: usize, r: u8, g: u8, b: u8) {
        let index = (y * self.width + x) * 3;
        self.pixels[index] = r;
        self.pixels[index + 1] = g;
        self.pixels[index + 2] = b;
    }

    pub fn save_as_ppm(&self, filename: &str) -> io::Result<()> {
        let mut file = File::create(filename)?;
        writeln!(file, "P6\n{} {}\n255", self.width, self.height)?;

        file.write_all(&self.pixels)?;
        Ok(())
    }
}
