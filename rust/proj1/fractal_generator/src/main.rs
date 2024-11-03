mod image;
mod complex;
mod fractal;

use fractal::mandelbrot;

fn main() {
    let image = mandelbrot(2000, 1200, 1000);
    image.save_as_ppm("mandelbrot.ppm").expect("Failed to save image");
}
