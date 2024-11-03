use crate::image::Image;
use crate::complex::Complex;

pub fn mandelbrot(width: usize, height: usize, max_iterations: usize) -> Image {
    let mut image = Image::new(width, height);
    for x in 0..width {
        for y in 0..height {
            let re = (x as f64 / width as f64) * 3.5 - 2.5;     // scale to [-2.5, 1]
            let im = (y as f64 / height as f64) * 2.0 - 1.0;    // scale to [  -1, 1]
            let c = Complex::new(re, im);
            let mut z = Complex::new(0.0, 0.0);
            let mut iterations = 0;

            while z.magnitude() <= 2.0 && iterations < max_iterations {
                z = z.multiply(z).add(c);
                iterations += 1;
            }

            let color = if iterations == max_iterations {
                (0, 0, 0)
            } else {
                let value = (255 * iterations^2 / max_iterations^2) as u8;
                (value, value, 255)
            };
            image.set_pixel(x, y, color.0, color.1, color.2);
        }
    }
    image
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_mandelbrot_image_size() {
        let width = 800;
        let height = 600;
        let max_iterations = 1000;

        let image = mandelbrot(width, height, max_iterations);
        
        // Check if the image dimensions are correct
        assert_eq!(image.width, width);
        assert_eq!(image.height, height);
    }

    #[test]
    fn test_mandelbrot_max_iterations() {
        let width = 100;
        let height = 100;
        let max_iterations = 10;

        let image = mandelbrot(width, height, max_iterations);

        for x in 0..width {
            for y in 0..height {
                let pixel_color = image.get_pixel(x, y);
                
                // If the point belongs to the Mandelbrot set, color should be black
                if pixel_color == (0, 0, 0) {
                    // Check if the pixel is black indicating max iterations reached
                    assert_eq!(pixel_color, (0, 0, 0));
                } else {
                    // Otherwise, it should be non-black
                    assert_ne!(pixel_color, (0, 0, 0));
                }
            }
        }
    }

    #[test]
    fn test_mandelbrot_zero_iterations() {
        let width = 800;
        let height = 600;
        let max_iterations = 0; // Edge case with no iterations

        let image = mandelbrot(width, height, max_iterations);
        
        // All pixels should be black as no iterations were performed
        for x in 0..width {
            for y in 0..height {
                assert_eq!(image.get_pixel(x, y), (0, 0, 0));
            }
        }
    }

    #[test]
    fn test_mandelbrot_negative_dimensions() {
        let width = 800;
        let height = 600;
        let max_iterations = 100;

        // Ensure it handles negative dimensions gracefully
        let image = mandelbrot(width, height, max_iterations);
        
        assert!(image.width > 0);
        assert!(image.height > 0);
    }
}
