#pragma once
#include <iostream>

class BowlingGame {
public:
	void roll(int pins) {
		score += bonus[0] * pins;
		bonus[0] = bonus[1];
		bonus[1] = 0;

		if (++turn > 20)
			return;

		score += pins;
		if (isfirst && pins == 10) {
			bonus[0]++;
			bonus[1]++;
			turn++;
			return;
		}

		if (!isfirst && prev + pins == 10)
			bonus[0]++;

		isfirst ^= true;
		prev = pins;
	}

	int getScore() {
		return score;
	}

private:
	int score = 0;
	int turn = 0;
	int prev = 0;
	bool isfirst = true;
	int bonus[2] = {0, 0};
};

