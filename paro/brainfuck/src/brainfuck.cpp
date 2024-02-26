#include "Brainfuck.hpp"

#include <stdio.h>
#include <stdlib.h>

#include <algorithm>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

#include "Memory.hpp"

using namespace std;
using string_iterator = string::const_iterator;

string_iterator getPositionOfLastCommandInLoop(
    string_iterator command_position) {
  int counter = 0;

  do {
    switch (*command_position) {
      case '[':
        counter++;
        break;
      case ']':
        counter--;
        break;
      default:
        break;
    }
    command_position++;
  } while (counter);

  return command_position - 1;
}

bool isLooping(Memory &memory) { return memory.get() != 0; }

void savePositionOfLoopStart(stack<string_iterator> &commands_positions,
                             string_iterator command_position) {
  commands_positions.push(command_position);
}

string_iterator getPositionOfCommandAtLoopStart(
    stack<string_iterator> &commands_positions) {
  string_iterator command_position = commands_positions.top() - 1;
  commands_positions.pop();

  return command_position;
}

std::string Brainfuck::interpret(Code const &code, Input const &input) const {
  Memory memory;
  std::string result;

  string_iterator in(input.begin());
  string_iterator command_position(code.begin());

  stack<string_iterator> commands_positions;

  for (; command_position < code.end(); command_position++) {
    switch (*command_position) {
      case '.':
        result += memory.get();
        break;

      case ',':
        memory.set(*in++);
        break;

      case '+':
        memory.increment();
        break;

      case '-':
        memory.decrement();
        break;

      case '>':
        memory.moveRight();
        break;

      case '<':
        memory.moveLeft();
        break;

      case '[':
        savePositionOfLoopStart(commands_positions, command_position);
        if (!isLooping(memory)) {
          command_position = getPositionOfLastCommandInLoop(command_position);
        }
        break;

      case ']': {
        string_iterator loop_start(
            getPositionOfCommandAtLoopStart(commands_positions));
        if (isLooping(memory)) {
          command_position = loop_start;
        }
        break;
      }
      
      default:
        break;
    }
  }

  return result;
}