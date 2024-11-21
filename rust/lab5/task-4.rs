fn order_weight(s: &str) -> String {
    let mut numbers: Vec<&str> = s.split_whitespace().collect();
    numbers.sort_by(|a, b| {
        let sum_a = a.chars().map(|c| c.to_digit(10).unwrap()).sum::<u32>();
        let sum_b = b.chars().map(|c| c.to_digit(10).unwrap()).sum::<u32>();
        sum_a.cmp(&sum_b).then_with(|| a.cmp(b))
    });
    numbers.join(" ")
}

// Unit tests
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(order_weight("56 65 74 100 99 68 86 180 90"), "100 180 90 56 65 74 68 86 99");
    }

    #[test]
    fn test_example_2() {
        assert_eq!(order_weight("1 2 3 4 5 6 7 8 9 10"), "1 10 2 3 4 5 6 7 8 9");
    }

    #[test]
    fn test_example_3() {
        assert_eq!(order_weight("11 10 101 100 1000"), "10 100 1000 101 11");
    }

    #[test]
    fn test_single_number() {
        assert_eq!(order_weight("100"), "100");
    }

    #[test]
    fn test_empty_string() {
        assert_eq!(order_weight(""), "");
    }

    #[test]
    fn test_same_weight_numbers() {
        assert_eq!(order_weight("11 2 20 101"), "101 11 2 20");
    }

    #[test]
    fn test_numbers_with_leading_trailing_spaces() {
        assert_eq!(order_weight(" 56   65  74 100 "), "100 56 65 74");
    }

    #[test]
    fn test_numbers_with_multiple_spaces() {
        assert_eq!(order_weight("56  65 74  100 99   "), "100 56 65 74 99");
    }
}