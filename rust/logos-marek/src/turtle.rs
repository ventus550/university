pub mod turtle {
    use std::fmt;

    #[derive(Debug, Clone, PartialEq, Eq)]
    pub struct Pixel {
        red: u8,
        green: u8,
        blue: u8
    }

    impl Pixel {
        // Useful colors
        pub const BLACK : Pixel = Pixel::new(0, 0, 0);
        pub const WHITE : Pixel = Pixel::new(255, 255, 255);
        pub const RED : Pixel = Pixel::new(255, 0, 0);
        pub const GREEN : Pixel = Pixel::new(0, 255, 0);
        pub const BLUE : Pixel = Pixel::new(0, 0, 255);
    
        /**
         * Create new pixel using RGB
         */
        pub const fn new(red: u8, green: u8, blue: u8) -> Pixel {
            Pixel {red, green, blue}
        }

        /**
         * Sets pixel color using RGB
         */
        pub fn set_rgb(&mut self, red: u8, green: u8, blue: u8) -> &mut Self {
            self.red = red;
            self.green = green;
            self.blue = blue;
            self
        }
    }

    impl From<String> for Pixel {
        fn from(s: String) -> Self {
            let colors = s
                .split(|c: char| !c.is_numeric())
                .filter_map(|x| x.parse().ok())
                .collect::<Vec<u8>>();

            Pixel::new(colors[0], colors[1], colors[2])
        }
    }

    /**
     * Implementation for pixel displaying
     */
    impl fmt::Display for Pixel {
        fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
            write!(f, "rgb({}, {}, {})", self.red, self.green, self.blue)
        }
    }

    #[derive(Debug)]
    pub struct Turtle {
        pub pen: bool,
        pub angle: f64,
        pub x: f64,
        pub y: f64,
        pub color: Pixel,
    }

    impl Turtle {
        pub fn new() -> Turtle {
            Turtle{pen: true, angle: 0.0, x: 0.0, y: 0.0, color: Pixel::BLACK}
        }

        pub fn fd(&mut self, d: f64) {
            self.x += d * self.angle.sin();
            self.y += d * -self.angle.cos();
        }

        pub fn turn(&mut self, deg: f64) {
            self.angle = (self.angle + deg.to_radians()) % (2.0 * std::f64::consts::PI);
            if self.angle < 0.0 {
                self.angle += 2.0 * std::f64::consts::PI;
            }
        }

        pub fn set_pen(&mut self, pen: bool) {
            self.pen = pen;
        }

        pub fn set_color(&mut self, color: Pixel) {
            self.color = color;
        }
    }
}