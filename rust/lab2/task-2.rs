fn longest(a1: &str, a2: &str) -> String {
    let mut combined: Vec<char> = a1.chars().chain(a2.chars()).collect();
    combined.sort();
    combined.dedup();
    combined.into_iter().collect()
}

#[test]
fn test_aretheyhere_yestheyarehere() {
	testing("aretheyhere", "yestheyarehere", "aehrsty");
}

#[test]
fn test_loopingisfunbutdangerous_lessdangerousthancoding() {
	testing("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu");
}

#[test]
fn test_inmanylanguages_theresapairoffunctions() {
	testing("inmanylanguages", "theresapairoffunctions", "acefghilmnoprstuy");
}

#[test]
fn test_xyaabbbccccdefww_xxxxyyyyabklmopq() {
	testing("xyaabbbccccdefww", "xxxxyyyyabklmopq", "abcdefklmopqwxy");
}

#[test]
fn test_alphabet() {
	testing("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz");
}