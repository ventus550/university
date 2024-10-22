use std::collections::HashMap;

struct Cipher {
    encode_map: HashMap<char, char>,
    decode_map: HashMap<char, char>,
}

impl Cipher {
    fn new(map1: &str, map2: &str) -> Cipher {
        let encode_map: HashMap<char, char> = map1.chars().zip(map2.chars()).collect();
        let decode_map: HashMap<char, char> = map2.chars().zip(map1.chars()).collect();
        Cipher {
            encode_map,
            decode_map,
        }
    }

    fn encode(&self, string: &str) -> String {
        string.chars()
            .map(|ch| *self.encode_map.get(&ch).unwrap_or(&ch))  // Use the encode map or leave unchanged
            .collect()
    }

    fn decode(&self, string: &str) -> String {
        string.chars()
            .map(|ch| *self.decode_map.get(&ch).unwrap_or(&ch))  // Use the decode map or leave unchanged
            .collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_encode() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode("abc"), "eta");      // 'a' -> 'e', 'b' -> 't', 'c' -> 'a'
        assert_eq!(cipher.encode("xyz"), "qxz");      // 'x' -> 'q', 'y' -> 'x', 'z' -> 'z'
        assert_eq!(cipher.encode("aeiou"), "eirfg");  // Vowels substitution check
    }

    #[test]
    fn test_decode() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.decode("eta"), "abc");      // Reverse substitution 'e' -> 'a', 't' -> 'b', 'a' -> 'c'
        assert_eq!(cipher.decode("qxz"), "xyz");      // Reverse 'q' -> 'x', 'x' -> 'y', 'z' -> 'z'
        assert_eq!(cipher.decode("eirfg"), "aeiou");  // Vowels back to original
    }

    #[test]
    fn test_encode_with_non_alphabet() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode("abc123"), "eta123");  // Numbers should remain unchanged
    }

    #[test]
    fn test_decode_with_non_alphabet() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.decode("eta123"), "abc123");  // Numbers should remain unchanged
    }

    #[test]
    fn test_empty_string() {
        let map1 = "abcdefghijklmnopqrstuvwxyz";
        let map2 = "etaoinshrdlucmfwypvbgkjqxz";
        let cipher = Cipher::new(map1, map2);

        assert_eq!(cipher.encode(""), "");  // Empty input should return empty output
        assert_eq!(cipher.decode(""), "");  // Empty input should return empty output
    }
}
