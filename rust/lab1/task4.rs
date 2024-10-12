fn printer_error(s: &str) -> String {
	let valid_colors: Vec<char> = "abcdefghijklm".chars().collect();
	let valid_set: std::collections::HashSet<char> = valid_colors.into_iter().collect();
	let error_count = s.chars().filter(|&c| !valid_set.contains(&c)).count();
	let total_length = s.len();

	format!("{}/{}", error_count, total_length)
}

fn main() {
	assert_eq!(&printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "3/56");
	assert_eq!(&printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"), "6/60");
	assert_eq!(&printer_error("kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"), "11/65");
}
