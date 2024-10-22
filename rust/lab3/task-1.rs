fn row_sum_odd_numbers(n: i64) -> i64 {
    n * n * n
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_row_1() {
        assert_eq!(row_sum_odd_numbers(1), 1); // 1^3 = 1
    }

    #[test]
    fn test_row_2() {
        assert_eq!(row_sum_odd_numbers(2), 8); // 2^3 = 8
    }

    #[test]
    fn test_row_3() {
        assert_eq!(row_sum_odd_numbers(3), 27); // 3^3 = 27
    }

    #[test]
    fn test_row_4() {
        assert_eq!(row_sum_odd_numbers(4), 64); // 4^3 = 64
    }

    #[test]
    fn test_row_5() {
        assert_eq!(row_sum_odd_numbers(5), 125); // 5^3 = 125
    }
}
