fn wave(s: &str) -> Vec<String> {
    let mut result = Vec::new();
    for (i, c) in s.chars().enumerate() {
        if c.is_whitespace() {
            continue;
        }
        let mut chars: Vec<char> = s.chars().collect();
        chars[i] = c.to_uppercase().next().unwrap();
        result.push(chars.into_iter().collect());
    }
    result
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_wave_hello() {
        assert_eq!(
            wave("hello"),
            vec!["Hello", "hEllo", "heLlo", "helLo", "hellO"]
        );
    }

    #[test]
    fn test_wave_empty() {
        assert_eq!(wave(""), Vec::<String>::new());
    }

    #[test]
    fn test_wave_spaces() {
        assert_eq!(wave("a b"), vec!["A b", "a B"]);
    }

    #[test]
    fn test_wave_no_spaces() {
        assert_eq!(
            wave("rust"),
            vec!["Rust", "rUst", "ruSt", "rusT"]
        );
    }

    #[test]
    fn test_wave_with_leading_spaces() {
        assert_eq!(
            wave(" rust"),
            vec![" Rust", " rUst", " ruSt", " rusT"]
        );
    }
}