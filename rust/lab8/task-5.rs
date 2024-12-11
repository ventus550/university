fn first_n_smallest(arr: &[i32], n: usize) -> Vec<i32> {
    let mut sorted_arr = arr.to_vec();
    sorted_arr.sort_unstable();

    let mut smallest_n = Vec::new();
    let mut count = 0;
    
    for &val in sorted_arr.iter() {
        if count < n {
            smallest_n.push(val);
            count += 1;
        }
    }

    let mut result = Vec::new();
    let mut remaining = smallest_n.clone();
    
    for &val in arr.iter() {
        if remaining.contains(&val) {
            result.push(val);
            if let Some(pos) = remaining.iter().position(|&x| x == val) {
                remaining.remove(pos);
            }
        }
        if result.len() == n {
            break;
        }
    }

    result
}



#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[1,2,3,4,5],3), [1,2,3]);
	}
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[5,4,3,2,1],3), [3,2,1]);
	}
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[1,2,3,1,2],3), [1,2,1]);
	}
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[1,2,3,-4,0],3), [1,-4,0]);
	}
    fn test_basic_1() {
        assert_eq!(first_n_smallest(&[1,2,3,4,5],0), []);
    }
}
