#define CATCH_CONFIG_MAIN
#include <string>
#include "../include/catch.hpp"
#include "../include/stringConverter.hpp"
#include "../include/debugPrinter.hpp"

#include "../src/Brainfuck.hpp"

TEST_CASE( "Brainfuck interpreter test cases", "[interp]" ) {

    Brainfuck interpreter;

    SECTION( "empty code evaluates to empty result" ) {
        Code code{convertToString("")};
        Input input{convertToString("")};
        REQUIRE( interpreter.interpret(code, input) == convertToString(""));
    }

    SECTION( "outputting memory without any prior operations yields zeroes" ) {
        Code code{convertToString("..........")};
        Input input{convertToString("")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("\0\0\0\0\0\0\0\0\0\0") );
    }

    SECTION( "streaming input to output works correctly" ) {
        Code code{convertToString(",.,..,...,....")};
        Input input{convertToString("abcd")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("abbcccdddd") );
    }

    SECTION( "incrementing/decrementing at memory pointer results in correct numbers" ) {
        Code code{convertToString(",.+.++.+++.---.--.-.")};
        Input input{convertToString("\1")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("\1\2\4\7\4\2\1") );
    }

    SECTION( "memory can be traversed" ) {
        Code code{convertToString(",>,>,>,<<<.>.>.>.<.<.<.")};
        Input input{convertToString("abcd")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("abcdcba") );
    }

    SECTION( "simple loops' steps are stepped through" ) {
        Code code{convertToString(",[.-]")};
        Input input{convertToString("\5")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("\5\4\3\2\1") );
    }

    SECTION( "nested loops' are evaluated in order" ) {
        Code code{convertToString(",[.>+[.-]<-]")};
        Input input{convertToString("\5")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("\5\1\4\1\3\1\2\1\1\1") );
    }


    SECTION( "overflow test" ) {
        Code code{convertToString(",+.")};
        Input input{convertToString("\377")};

        REQUIRE( interpreter.interpret(code, input) == convertToString("\0") );
    }

    SECTION( "underflow test" ) {
        Code code{convertToString(",-.")};
        Input input{convertToString("\0")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("\377") );
    }

    SECTION( "comments are ignored" ) {
        Code code{convertToString("qwertyuiopasdfghjklzxcvbnm,.")};
        Input input{convertToString("a")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("a") );
    }

    SECTION( "empty loop" ) {
        Code code{convertToString("[]")};
        Input input{convertToString("")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("") );
    }

    SECTION( "self interpreter" ) {
        Code code{convertToString(
            ">>>+[[-]>>[-]++>+>+++++++[<++++>>++<-]++>>+>+>+++++[>++>++++++<<-]+>>>,<++[[>["
            "->>]<[>>]<<-]<[<]<+>>[>]>[<+>-[[<+>-]>]<[[[-]<]++<-[<+++++++++>[<->-]>>]>>]]<<"
            "]<]<[[<]>[[>]>>[>>]+[<<]<[<]<+>>-]>[>]+[->>]<<<<[[<<]<[<]+<<[+>+<<-[>-->+<<-[>"
            "+<[>>+<<-]]]>[<+>-]<]++>>-->[>]>>[>>]]<<[>>+<[[<]<]>[[<<]<[<]+[-<+>>-[<<+>++>-"
            "[<->[<<+>>-]]]<[>+<-]>]>[>]>]>[>>]>>]<<[>>+>>+>>]<<[->>>>>>>>]<<[>.>>>>>>>]<<["
            ">->>>>>]<<[>,>>>]<<[>+>]<<[+<<]<]"
        )};
        Input input{convertToString(",.!a")};
        REQUIRE( interpreter.interpret(code, input) == convertToString("a") );
    }
}

