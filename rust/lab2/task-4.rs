fn count_red_beads(n: u32) -> u32 {
	n.saturating_sub(1) * 2
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_no_blue_beads() {
        assert_eq!(count_red_beads(0), 0);
    }

    #[test]
    fn test_one_blue_bead() {
        assert_eq!(count_red_beads(1), 0);
    }

    #[test]
    fn test_two_blue_beads() {
        assert_eq!(count_red_beads(2), 2);
    }

    #[test]
    fn test_three_blue_beads() {
        assert_eq!(count_red_beads(3), 4);
    }

    #[test]
    fn test_large_number_of_blue_beads() {
        assert_eq!(count_red_beads(10), 18);
    }
}
