fn longest_vowel_chain(s: &str) -> usize {
    let vowels = ['a', 'e', 'i', 'o', 'u'];
    s.chars()
        .map(|c| u8::from(vowels.contains(&c)))
        .scan(0, |state, x| {
            *state = if x == 1 { *state + 1 } else { 0 };
            Some(*state)
        })
        .max()
        .unwrap_or(0)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_example_1() {
        assert_eq!(longest_vowel_chain("codewarriors"), 2);
    }

    #[test]
    fn test_all_consonants() {
        assert_eq!(longest_vowel_chain("bcdfghjklmnpqrstvwxyz"), 0);
    }

    #[test]
    fn test_single_vowel() {
        assert_eq!(longest_vowel_chain("a"), 1);
    }

    #[test]
    fn test_single_consonant() {
        assert_eq!(longest_vowel_chain("b"), 0);
    }

    #[test]
    fn test_all_vowels() {
        assert_eq!(longest_vowel_chain("aeiou"), 5);
    }

    #[test]
    fn test_alternating_vowel_consonant() {
        assert_eq!(longest_vowel_chain("abecidofu"), 1);
    }

    #[test]
    fn test_vowel_clusters() {
        assert_eq!(longest_vowel_chain("aeiobcdou"), 4);
    }

    #[test]
    fn test_long_string_with_mixed_vowels() {
        assert_eq!(longest_vowel_chain("abracadabraaei"), 4);
    }

    #[test]
    fn test_long_vowel_chain_in_middle() {
        assert_eq!(longest_vowel_chain("xyzabcdiooooufgh"), 6);
    }

    #[test]
    fn test_multiple_equal_vowel_chains() {
        assert_eq!(longest_vowel_chain("aeiooxaeiou"), 5);
    }
    
    #[test]
    fn test_empty_string() {
        assert_eq!(longest_vowel_chain(""), 0);
    }
}