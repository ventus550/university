fn count_bits(n: i64) -> u32 {
    n.count_ones()
}

fn do_test(n: i64, expected: u32) {
	let actual = count_bits(n);
	assert_eq!(actual, expected,
		"expected {} but got {} for n = {}",
		expected, actual, n
	);
}

fn main() {
	do_test(0, 0);
	do_test(4, 1);
	do_test(7, 3);
	do_test(77231418, 14);
	do_test(12525589, 11);
	do_test(31, 5);
	do_test(417862, 7);
	do_test(89, 4);
	do_test(674259, 10);
	do_test(i64::MAX, 63)
}
