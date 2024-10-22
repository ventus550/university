fn number(bus_stops: &[(i32, i32)]) -> i32 {
    bus_stops.iter().fold(0, |people_on_bus, (on, off)| people_on_bus + on - off)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_case_1() {
        // Example: 10 people get on at the first stop, and 0 get off
        // 3 get on at the second stop, 5 get off
        // 2 get on at the third stop, 1 gets off
        // Final result: 10 + 3 + 2 - 5 - 1 = 9 people on the bus
        let bus_stops = [(10, 0), (3, 5), (2, 1)];
        assert_eq!(number(&bus_stops), 9);
    }

    #[test]
    fn test_case_2() {
        // People getting on and off at different stops
        let bus_stops = [(3, 0), (9, 1), (4, 10), (12, 2), (6, 1), (7, 10)];
        // Final result: 3 + 9 + 4 + 12 + 6 + 7 - (1 + 10 + 2 + 1 + 10) = 17
        assert_eq!(number(&bus_stops), 17);
    }

    #[test]
    fn test_case_3() {
        // Edge case where nobody gets on or off
        let bus_stops = [(0, 0), (0, 0), (0, 0)];
        // Final result: 0
        assert_eq!(number(&bus_stops), 0);
    }

    #[test]
    fn test_case_4() {
        // Only people get off
        let bus_stops = [(10, 0), (0, 10)];
        // Final result: 10 - 10 = 0
        assert_eq!(number(&bus_stops), 0);
    }

    #[test]
    fn test_case_5() {
        // Final stop has people remaining on the bus
        let bus_stops = [(5, 0), (3, 2), (4, 1), (2, 1)];
        // Final result: 5 + 3 + 4 + 2 - (2 + 1 + 1) = 10
        assert_eq!(number(&bus_stops), 10);
    }
}
