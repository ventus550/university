fn summy(strng: &str) -> i32 {
    strng.split_whitespace()
         .map(|x| x.parse::<i32>().unwrap())
         .sum()
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_number() {
        assert_eq!(summy("5"), 5);
    }

    #[test]
    fn test_multiple_numbers() {
        assert_eq!(summy("1 2 3"), 6);
    }

    #[test]
    fn test_large_numbers() {
        assert_eq!(summy("100 200 300"), 600);
    }

    #[test]
    fn test_negative_numbers() {
        assert_eq!(summy("-1 -2 -3"), -6);
    }

    #[test]
    fn test_mixed_sign_numbers() {
        assert_eq!(summy("-10 20 -30 40"), 20);
    }
}