fn solution(n: f64) -> f64 {
    ( (n * 2.0).round() ) / 2.0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(solution(4.2), 4.0);
    }

    #[test]
    fn test_example_2() {
        assert_eq!(solution(4.3), 4.5);
    }

    #[test]
    fn test_example_3() {
        assert_eq!(solution(4.6), 4.5);
    }

    #[test]
    fn test_example_4() {
        assert_eq!(solution(4.8), 5.0);
    }

    #[test]
    fn test_example_5() {
        assert_eq!(solution(4.75), 5.0);
    }

    #[test]
    fn test_example_6() {
        assert_eq!(solution(5.2), 5.0);
    }

    #[test]
    fn test_example_7() {
        assert_eq!(solution(5.3), 5.5);
    }

    #[test]
    fn test_example_8() {
        assert_eq!(solution(5.7), 5.5);
    }

    #[test]
    fn test_example_9() {
        assert_eq!(solution(5.8), 6.0);
    }

    #[test]
    fn test_zero() {
        assert_eq!(solution(0.0), 0.0);
    }
}   