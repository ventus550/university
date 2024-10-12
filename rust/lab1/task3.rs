use std::f64::consts::PI;

fn square_area_to_circle(size:f64) -> f64 {
	(PI * size) / 4.0
}

fn assert_close(a:f64, b:f64, epsilon:f64) {
	assert!( (a-b).abs() < epsilon, "Expected: {}, got: {}",b,a);
}

fn main() {
	assert_close(square_area_to_circle(9.0), 7.0685834705770345, 1e-8);
	assert_close(square_area_to_circle(20.0), 15.70796326794897, 1e-8);
}
