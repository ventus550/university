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
