use rand::prelude::*;

fn string_to_number(s: &str) -> i32 {
    match s.parse::<i32>() {
        Ok(num) => num,
        Err(_) => 0,
    }
}

fn main() {
	assert_eq!(string_to_number("1234"), 1234);
	assert_eq!(string_to_number("605"), 605);
	assert_eq!(string_to_number("1405"), 1405);
	assert_eq!(string_to_number("-7"), -7);

	let mut rng = thread_rng();
	for _ in 0..5 {
		let num : i32 = rng.gen();
		let input = num.to_string();
		assert_eq!(string_to_number(&input), num);
	}

}
