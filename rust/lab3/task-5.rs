fn last_digit(a: &str, b: &str) -> i32 {
    let a = a.chars().last().unwrap().to_digit(10).unwrap();
    
    if b == "0" {
        return 1;
    }

    let cycles = [
        vec![0],             
        vec![1],             
        vec![2, 4, 8, 6],    
        vec![3, 9, 7, 1],    
        vec![4, 6],          
        vec![5],             
        vec![6],             
        vec![7, 9, 3, 1],    
        vec![8, 4, 2, 6],    
        vec![9, 1],          
    ];

    let cycle = &cycles[a as usize];
    let cycle_len = cycle.len() as u128;

    let mut reduced_b = 0;
    for digit in b.chars() {
        let digit_val = digit.to_digit(10).unwrap() as u128;
        reduced_b = (reduced_b * 10 + digit_val) % cycle_len;
    }

    let effective_exponent = if reduced_b == 0 { cycle_len } else { reduced_b };
    cycle[(effective_exponent as usize - 1) % cycle.len()] as i32
}


#[test]
fn t1() {
  assert_eq!(last_digit("4", "1"), 4);
}

#[test]
fn t2() {
  assert_eq!(last_digit("4", "2"), 6);
}

#[test]
fn t3() {
  assert_eq!(last_digit("9", "7"), 9);
}

#[test]
fn t4() {
  assert_eq!(last_digit("10","10000000000"), 0);
}

#[test]
fn t5() {
  assert_eq!(last_digit("1606938044258990275541962092341162602522202993782792835301376","2037035976334486086268445688409378161051468393665936250636140449354381299763336706183397376"), 6);
}
#[test]
fn t6() {
  assert_eq!(last_digit("3715290469715693021198967285016729344580685479654510946723", "68819615221552997273737174557165657483427362207517952651"), 7);
}