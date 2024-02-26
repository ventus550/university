#include <stdio.h>
#include <inttypes.h>


int solve(uint64_t x) {
	uint64_t mask = 0x0F0F0F0F0F0F0F0F;
	uint64_t even = x;
			 even = even & mask;
	uint64_t odd = x;
			 odd = odd >> 4;
			 odd = odd & mask;


	//suma 4-bitowców
	uint64_t eshifted = even;
			 eshifted = eshifted >> 8;
			 even = even + eshifted;

	uint64_t oshifted = odd;
			 oshifted = oshifted >> 8;
			 odd = odd + oshifted;

	
	//suma 8-bitowców
			 eshifted = even;
			 eshifted = eshifted >> 16;
			 even = even + eshifted;
			 
			 oshifted = odd;
			 oshifted = oshifted >> 16;
			 odd = odd + oshifted;


	//suma 16-bitowców
			 eshifted = even;
			 eshifted = eshifted >> 32;
			 even = even + eshifted;
			 
			 oshifted = odd;
			 oshifted = oshifted >> 32;
			 odd = odd + oshifted;
	//printf("odd: %d\n", odd);
	//printf("evem: %d\n", even);
	uint64_t sum = even - odd;
	//printf("sum: %d\n", sum);
	
	if (sum > 0x1FF) {
		sum = sum + 136;
	}
	sum &= 0xFF;
	
	//printf("+136: %d\n", sum);
	mask = 0xF;
	even = sum & mask;
	odd = sum >> 4;
	//printf("shift: %d %d\n", even, odd);

	sum = even - odd;
	//printf("shift: %d %d\n", even, odd);

	if (sum > 0x1FF) {
		sum = sum + 17;
	}

	return sum;	
}

// 0x00AA00BB00CC00DD
int main(){
	uint64_t x = 0x0f0f0f0f0f0f0f0f;
	printf("solve: %d => %d\n", solve(x), x % 17);
}