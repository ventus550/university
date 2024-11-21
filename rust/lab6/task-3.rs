fn comp(a: Vec<i64>, b: Vec<i64>) -> bool {
    if a.len() != b.len() {
        return false;
    }

    let mut a_squared_sorted: Vec<i64> = a.iter().map(|&x| x * x).collect();
    let mut b_sorted = b.clone();
    a_squared_sorted.sort();
    b_sorted.sort();
    a_squared_sorted == b_sorted
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_arrays() {
        let a = vec![121, 144, 19, 161, 19, 144, 19, 11];
        let b = vec![121, 14641, 20736, 361, 25921, 361, 20736, 361];
        assert_eq!(comp(a, b), true);
    }

    #[test]
    fn test_invalid_arrays_1() {
        let a = vec![121, 144, 19, 161, 19, 144, 19, 11];
        let b = vec![132, 14641, 20736, 361, 25921, 361, 20736, 361];
        assert_eq!(comp(a, b), false);
    }

    #[test]
    fn test_invalid_arrays_2() {
        let a = vec![121, 144, 19, 161, 19, 144, 19, 11];
        let b = vec![121, 14641, 20736, 36100, 25921, 361, 20736, 361];
        assert_eq!(comp(a, b), false);
    }

    #[test]
    fn test_empty_arrays() {
        let a: Vec<i64> = Vec::new();
        let b: Vec<i64> = Vec::new();
        assert_eq!(comp(a, b), true);
    }

    #[test]
    fn test_mismatched_lengths() {
        let a = vec![1, 2, 3];
        let b = vec![1, 4];
        assert_eq!(comp(a, b), false);
    }
}