fn largest_difference(data: &[i32]) -> usize {
    let mut max_diff = 0;

    for i in 0..data.len() {
        for j in (i..data.len()).rev() {
            if data[i] <= data[j] {
                max_diff = max_diff.max(j - i);
                break;
            }
        }
    }

    max_diff
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_case() {
        let data = vec![1, 2, 3];
        assert_eq!(largest_difference(&data), 2);
    }

    #[test]
    fn test_no_difference() {
        let data = vec![3, 2, 1];
        assert_eq!(largest_difference(&data), 0);
    }

    #[test]
    fn test_multiple_differences() {
        let data = vec![1, 2, 1, 2, 1];
        assert_eq!(largest_difference(&data), 4);
    }

    #[test]
    fn test_all_equal() {
        let data = vec![2, 2, 2, 2];
        assert_eq!(largest_difference(&data), 3);
    }

    #[test]
    fn test_single_element() {
        let data = vec![1];
        assert_eq!(largest_difference(&data), 0);
    }
}