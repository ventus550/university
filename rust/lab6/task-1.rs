fn coin_combo(cents: u64) -> [u64; 4] {
    let quarters = cents / 25;
    let remainder_after_quarters = cents % 25;

    let dimes = remainder_after_quarters / 10;
    let remainder_after_dimes = remainder_after_quarters % 10;

    let nickels = remainder_after_dimes / 5;
    let pennies = remainder_after_dimes % 5;

    [pennies, nickels, dimes, quarters]
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_coin_combo_1() {
        assert_eq!(coin_combo(6), [1, 1, 0, 0]);
    }

    #[test]
    fn test_coin_combo_2() {
        assert_eq!(coin_combo(41), [1, 1, 1, 1]);
    }

    #[test]
    fn test_coin_combo_3() {
        assert_eq!(coin_combo(99), [4, 0, 2, 3]);
    }

    #[test]
    fn test_coin_combo_4() {
        assert_eq!(coin_combo(0), [0, 0, 0, 0]);
    }

    #[test]
    fn test_coin_combo_5() {
        assert_eq!(coin_combo(25), [0, 0, 0, 1]);
    }
}