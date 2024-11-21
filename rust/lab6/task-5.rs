struct Sudoku {
    data: Vec<Vec<u32>>,
}

impl Sudoku {
    fn is_valid(&self) -> bool {
        let n = self.data.len();
        if n == 0 || (n as f64).sqrt().fract() != 0.0 || !self.data.iter().all(|row| row.len() == n) {
            return false;
        }
        let sqrt_n = (n as f64).sqrt() as usize;

        let valid = |items: Vec<u32>| -> bool {
            let mut seen = vec![false; n];
            items.into_iter().all(|v| v > 0 && v as usize <= n && !std::mem::replace(&mut seen[v as usize - 1], true))
        };

        (0..n).all(|i| valid(self.data[i].clone())) &&
        (0..n).all(|i| valid(self.data.iter().map(|row| row[i]).collect())) &&
        (0..n).step_by(sqrt_n).all(|r| 
            (0..n).step_by(sqrt_n).all(|c| 
                valid((0..sqrt_n).flat_map(|i| (0..sqrt_n).map(move |j| self.data[r + i][c + j])).collect())
            )
        )
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_sudoku() {
        let sudoku = Sudoku {
            data: vec![
                vec![7, 8, 4, 1, 5, 9, 3, 2, 6],
                vec![5, 3, 9, 6, 7, 2, 8, 4, 1],
                vec![6, 1, 2, 4, 3, 8, 7, 5, 9],
                vec![9, 2, 8, 7, 1, 5, 4, 6, 3],
                vec![3, 5, 7, 8, 4, 6, 1, 9, 2],
                vec![4, 6, 1, 9, 2, 3, 5, 8, 7],
                vec![8, 7, 6, 3, 9, 4, 2, 1, 5],
                vec![2, 4, 3, 5, 6, 1, 9, 7, 8],
                vec![1, 9, 5, 2, 8, 7, 6, 3, 4],
            ],
        };
        assert!(sudoku.is_valid());
    }

    #[test]
    fn test_invalid_sudoku_row() {
        let sudoku = Sudoku {
            data: vec![
                vec![7, 8, 4, 1, 5, 9, 3, 2, 6],
                vec![5, 3, 9, 6, 7, 2, 8, 4, 1],
                vec![6, 1, 2, 4, 3, 8, 7, 5, 9],
                vec![9, 2, 8, 7, 1, 5, 4, 6, 3],
                vec![3, 5, 7, 8, 4, 6, 1, 9, 2],
                vec![4, 6, 1, 9, 2, 3, 5, 8, 7],
                vec![8, 7, 6, 3, 9, 4, 2, 1, 5],
                vec![2, 4, 3, 5, 6, 1, 9, 7, 8],
                vec![1, 1, 5, 2, 8, 7, 6, 3, 4], // Invalid row (duplicate 1)
            ],
        };
        assert!(!sudoku.is_valid());
    }

    #[test]
    fn test_invalid_sudoku_column() {
        let sudoku = Sudoku {
            data: vec![
                vec![7, 8, 4, 1, 5, 9, 3, 2, 6],
                vec![5, 3, 9, 6, 7, 2, 8, 4, 1],
                vec![6, 1, 2, 4, 3, 8, 7, 5, 9],
                vec![9, 2, 8, 7, 1, 5, 4, 6, 3],
                vec![3, 5, 7, 8, 4, 6, 1, 9, 2],
                vec![4, 6, 1, 9, 2, 3, 5, 8, 7],
                vec![8, 7, 6, 3, 9, 4, 2, 1, 5],
                vec![2, 4, 3, 5, 6, 1, 9, 7, 8],
                vec![1, 9, 5, 2, 8, 7, 6, 3, 6], // Invalid column (duplicate 6)
            ],
        };
        assert!(!sudoku.is_valid());
    }


	#[test]
	fn good_sudoku() {
		let good_sudoku_1 = Sudoku{
			data: vec![
					vec![7,8,4, 1,5,9, 3,2,6],
					vec![5,3,9, 6,7,2, 8,4,1],
					vec![6,1,2, 4,3,8, 7,5,9],
	
					vec![9,2,8, 7,1,5, 4,6,3],
					vec![3,5,7, 8,4,6, 1,9,2],
					vec![4,6,1, 9,2,3, 5,8,7],
					
					vec![8,7,6, 3,9,4, 2,1,5],
					vec![2,4,3, 5,6,1, 9,7,8],
					vec![1,9,5, 2,8,7, 6,3,4]
				]
		};
		
		let good_sudoku_2 = Sudoku{
			data: vec![
					vec![1, 4,  2, 3],
					vec![3, 2,  4, 1],
			
					vec![4, 1,  3, 2],
					vec![2, 3,  1, 4],
				]
		};
		assert!(good_sudoku_1.is_valid());
		assert!(good_sudoku_2.is_valid());
	}
	
	#[test]
	fn bad_sudoku() {
		let bad_sudoku_1 = Sudoku{
			data: vec![
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
	
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
					
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
					vec![1,2,3, 4,5,6, 7,8,9],
				]
		};
		
		let bad_sudoku_2 = Sudoku{
			data: vec![
					vec![1,2,3,4,5],
					vec![1,2,3,4],
					vec![1,2,3,4],
					vec![1],
				]
		};
		assert!(!bad_sudoku_1.is_valid());
		assert!(!bad_sudoku_2.is_valid());
	}
}
