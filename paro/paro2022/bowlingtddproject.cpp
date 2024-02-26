#include "catch/catch.hpp"
#include "BowlingGame.h"
#include <iostream>


TEST_CASE("OneRoundWithZeroPinsShouldGiveScoreZero") {
	BowlingGame game;
	
	game.roll(0);
	game.roll(0);
	REQUIRE(game.getScore() == 0);
}

TEST_CASE("OneSpareFollowedBy0PinsShouldGiveScore10") {
    BowlingGame game;

    game.roll(5);
    game.roll(5);
    game.roll(0);
    game.roll(0);

    REQUIRE( game.getScore() == 10 );
}

TEST_CASE("FullGameWith1PinEachTimeShouldGiveScore20") {
	BowlingGame game;

	for (int i = 0; i < 20; ++i)
		game.roll(1);

	REQUIRE(game.getScore() == 20);
}

TEST_CASE("SpareShouldGiveABonus") {
	BowlingGame game;

	game.roll(6);
	game.roll(4);
	game.roll(1);
	game.roll(5);

	REQUIRE(game.getScore() == 17);
}

TEST_CASE("StrikeShouldGiveABonus") {
	BowlingGame game;

	game.roll(10);
	game.roll(3);
	game.roll(7);

	REQUIRE(game.getScore() == 30);
}

TEST_CASE("PerfectGameShouldScore300") {
	BowlingGame game;

	for (int i = 0; i < 12; ++i)
		game.roll(10);

	REQUIRE(game.getScore() == 300);
}