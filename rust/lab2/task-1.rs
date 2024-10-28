fn get_count(string: &str) -> usize {
    let vowels = "aeiou";
    string.chars().filter(|c| vowels.contains(*c)).count()
}

#[test]
fn test1() {
    assert_eq!(get_count("abracadabra"), 5);
}

#[test]
fn test2() {
    assert_eq!(get_count("hello world"), 3);
}

#[test]
fn test3() {
    assert_eq!(get_count("rust programming"), 4);
}

#[test]
fn test4() {
    assert_eq!(get_count("abcdefge"), 3);
}

#[test]
fn test5() {
    assert_eq!(get_count(""), 0);
}
