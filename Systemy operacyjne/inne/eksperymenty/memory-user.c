#include <stdio.h>
#include <stdlib.h>


int main(int argc, char *argv[]) {
	long long n = 1000000 * atoll(argv[1]);
	char *arr = (char*)malloc(n);
	while(1) {
		for(long long i = 0; i < n; i++) {
			arr[i] += 1;
		}
	}
}
