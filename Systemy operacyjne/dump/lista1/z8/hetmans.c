#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <iso646.h>

bool conflict(int board[], int k, int i) {

	int X = k - i,
		Y = abs(board[k] - board[i]);
	return X == Y or Y == 0;
}


bool isValid(int board[], int k) {

	for (int i = 0; i < k; i++) {
		if (conflict(board, k, i)) {return false;}
	}
	return true;
}



int main() {

	int n = 3, i = 0;

	for (int j = 0; j < n; j++) {
		pid = fork();
		
	}


	return 0;
}