#include "../include/catch.hpp"
#include "../src/Memory.hpp"


TEST_CASE( "initially memory cells are set to 0", "[memory]" ) {
    Memory memory;
    REQUIRE( memory.get() == Memory::MemoryCell{0} );
}

TEST_CASE( "getting after setting gives the same value", "[memory]" ) {
    Memory memory;
    constexpr auto value = 42;
    memory.set(value);
    REQUIRE( memory.get() == value );
}


TEST_CASE( "increment", "[memory]" ) {
    Memory memory;
    memory.increment();
    REQUIRE( memory.get() == 1 );
}


TEST_CASE( "decrement", "[memory]" ) {
    Memory memory;
    constexpr auto value = 43;
    memory.set(value);
    memory.decrement();
    REQUIRE( memory.get() == 42 );
}


TEST_CASE( "memory position can be moved around", "[memory]" ) {
    Memory memory;
    constexpr auto valueA = 21;
    constexpr auto valueB = 37;

    memory.set(valueA);
    memory.moveRight();
    memory.set(valueB);
    memory.moveLeft();

    REQUIRE( memory.get() == valueA );
    memory.moveRight();
    REQUIRE( memory.get() == valueB );
}

SCENARIO( "getting after setting gives the same value", "[memory-scen]" ) {

    GIVEN( "memory and a value" ) {
        Memory memory;
        constexpr auto value = 42;

        WHEN ("we set the value") {
            memory.set(value);

            THEN ( "getting value yields same value" ) {
                REQUIRE( memory.get() == value );
            }
        }
    }
}
