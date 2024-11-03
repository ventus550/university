use std::fs::File;
use std::io::{self, Write};

pub struct Image {
    pub width: usize,
    pub height: usize,
    pub pixels: Vec<u8>,
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

    #[allow(dead_code)]
    pub fn get_pixel(&self, x: usize, y: usize) -> (u8, u8, u8) {
        let index = (y * self.width + x) * 3;
        (self.pixels[index], self.pixels[index + 1], self.pixels[index + 2])
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_image_creation() {
        let width = 800;
        let height = 600;
        let image = Image::new(width, height);
        
        assert_eq!(image.width, width);
        assert_eq!(image.height, height);
        assert_eq!(image.pixels.len(), width * height * 3);
    }

    #[test]
    fn test_set_and_get_pixel() {
        let width = 100;
        let height = 100;
        let mut image = Image::new(width, height);

        image.set_pixel(0, 0, 255, 0, 0); // Set pixel at (0, 0) to red
        assert_eq!(image.get_pixel(0, 0), (255, 0, 0));

        image.set_pixel(1, 1, 0, 255, 0); // Set pixel at (1, 1) to green
        assert_eq!(image.get_pixel(1, 1), (0, 255, 0));

        image.set_pixel(2, 2, 0, 0, 255); // Set pixel at (2, 2) to blue
        assert_eq!(image.get_pixel(2, 2), (0, 0, 255));
    }

    #[test]
    fn test_save_as_ppm() {
        let width = 10;
        let height = 10;
        let mut image = Image::new(width, height);
        
        // Set a few pixels to different colors
        image.set_pixel(0, 0, 255, 0, 0); // Red
        image.set_pixel(1, 1, 0, 255, 0); // Green
        image.set_pixel(2, 2, 0, 0, 255); // Blue

        // The file will be created but not checked here; you can verify manually or check file contents in more sophisticated tests
        assert!(image.save_as_ppm("test_image.ppm").is_ok());
    }
}
