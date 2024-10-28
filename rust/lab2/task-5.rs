fn gimme_the_letters(sp: &str) -> String {
    let chars: Vec<char> = sp.split('-').collect::<Vec<&str>>().into_iter()
        .map(|x| x.chars().next().unwrap())
        .collect();
    
    let (start, end) = (chars[0], chars[1]);
    (start..=end).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_a_to_z() {
        assert_eq!(gimme_the_letters("a-z"), "abcdefghijklmnopqrstuvwxyz");
    }

    #[test]
    fn test_h_to_o() {
        assert_eq!(gimme_the_letters("h-o"), "hijklmno");
    }

    #[test]
    fn test_Q_to_Z() {
        assert_eq!(gimme_the_letters("Q-Z"), "QRSTUVWXYZ");
    }

    #[test]
    fn test_J_to_J() {
        assert_eq!(gimme_the_letters("J-J"), "J");
    }

    #[test]
    fn test_m_to_r() {
        assert_eq!(gimme_the_letters("m-r"), "mnopqr");
    }
}
