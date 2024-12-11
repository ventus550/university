fn part_list(arr: Vec<&str>) -> String {
    let mut result = Vec::new();

    for i in 1..arr.len() {
        let part1 = arr[..i].join(" ");
        let part2 = arr[i..].join(" ");
        result.push(format!("({}, {})", part1, part2));
    }

    result.join("")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_basic() {
        let arr = vec!["az", "toto", "picaro", "zone", "kiwi"];
        let expected = "(az, toto picaro zone kiwi)(az toto, picaro zone kiwi)(az toto picaro, zone kiwi)(az toto picaro zone, kiwi)";
        assert_eq!(part_list(arr), expected);
    }

    #[test]
    fn test_two_elements() {
        let arr = vec!["hello", "world"];
        let expected = "(hello, world)";
        assert_eq!(part_list(arr), expected);
    }

    #[test]
    fn test_three_elements() {
        let arr = vec!["a", "b", "c"];
        let expected = "(a, b c)(a b, c)";
        assert_eq!(part_list(arr), expected);
    }
}
