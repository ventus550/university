fn xo(string: &'static str) -> bool {
    let string = string.to_lowercase();
    let x_count = string.chars().filter(|&c| c == 'x').count();
    let o_count = string.chars().filter(|&c| c == 'o').count();
    x_count == o_count
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(xo("ooxx"), true);
    }

    #[test]
    fn test_example_2() {
        assert_eq!(xo("xooxx"), false);
    }

    #[test]
    fn test_example_3() {
        assert_eq!(xo("ooxXm"), true);
    }

    #[test]
    fn test_example_4() {
        assert_eq!(xo("zpzpzpp"), true);
    }

    #[test]
    fn test_example_5() {
        assert_eq!(xo("zzoo"), false);
    }

    #[test]
    fn test_empty_string() {
        assert_eq!(xo(""), true);
    }

    #[test]
    fn test_no_x_no_o() {
        assert_eq!(xo("abcdefg"), true);
    }

    #[test]
    fn test_mixed_case() {
        assert_eq!(xo("XxOo"), true);
    }

    #[test]
    fn test_all_x() {
        assert_eq!(xo("xxxxx"), false);
    }

    #[test]
    fn test_all_o() {
        assert_eq!(xo("ooooo"), false);
    }

    #[test]
    fn test_single_x() {
        assert_eq!(xo("x"), false);
    }

    #[test]
    fn test_single_o() {
        assert_eq!(xo("o"), false);
    }
}