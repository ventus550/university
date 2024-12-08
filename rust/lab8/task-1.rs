fn interpreter(code: &str, iterations: usize, width: usize, height: usize) -> String {
    let mut grid = vec![vec![0; width]; height];
    let mut pointer = (0, 0);
    let mut current_iteration = 0;
    
    let valid_commands: Vec<char> = code.chars().filter(|&c| "nesw*[]".contains(c)).collect();
    let mut code_pointer = 0;

    // Precompute the matching brackets for efficient jump
    let mut bracket_map: std::collections::HashMap<usize, usize> = std::collections::HashMap::new();
    let mut stack: Vec<usize> = Vec::new();

    for (i, &command) in valid_commands.iter().enumerate() {
        if command == '[' {
            stack.push(i);
        } else if command == ']' {
            let start = stack.pop().unwrap();
            bracket_map.insert(start, i);
            bracket_map.insert(i, start);
        }
    }

    while current_iteration < iterations && code_pointer < valid_commands.len() {
        let command = valid_commands[code_pointer];
        
        match command {
            'n' => {
                pointer.0 = (pointer.0 + height - 1) % height;
            }
            'e' => {
                pointer.1 = (pointer.1 + 1) % width;
            }
            's' => {
                pointer.0 = (pointer.0 + 1) % height;
            }
            'w' => {
                pointer.1 = (pointer.1 + width - 1) % width;
            }
            '*' => {
                let (r, c) = pointer;
                grid[r][c] = 1 - grid[r][c];
            }
            '[' => {
                let (r, c) = pointer;
                if grid[r][c] == 0 {
                    code_pointer = *bracket_map.get(&code_pointer).unwrap();
                }
            }
            ']' => {
                let (r, c) = pointer;
                if grid[r][c] != 0 {
                    code_pointer = *bracket_map.get(&code_pointer).unwrap();
                }
            }
            _ => {}
        }
        code_pointer += 1;
        current_iteration += 1;
    }

    grid.iter()
        .map(|row| row.iter().map(|&cell| cell.to_string()).collect::<Vec<String>>().join(""))
        .collect::<Vec<String>>()
        .join("\r\n")
}


#[test]
fn test_empty_code() {
    assert_eq!(interpreter("", 10, 3, 3), "000\r\n000\r\n000");
}

#[test]
fn test_no_iterations() {
    let code = "*";
    assert_eq!(interpreter(code, 0, 3, 3), "000\r\n000\r\n000");
}

#[test]
fn test_flip_single_cell() {
    let code = "*";
    assert_eq!(interpreter(code, 1, 3, 3), "100\r\n000\r\n000");
}

#[test]
fn test_move_and_flip() {
    let code = "*e*s*w*n";
    assert_eq!(interpreter(code, 5, 3, 3), "100\r\n010\r\n000");
}

#[test]
fn test_loops() {
    let code = "[*e]";
    assert_eq!(interpreter(code, 10, 3, 3), "111\r\n000\r\n000");
}

#[test]
fn test_loop_with_jump() {
    let code = "[*e]e";
    assert_eq!(interpreter(code, 5, 3, 3), "100\r\n010\r\n000");
}
