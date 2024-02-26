#include <stdio.h>
#include <inttypes.h>

uint64_t reverse(uint64_t num) {
	uint64_t mask1 = 0xFFFFFFFF;
	uint64_t mask2 = 0xFFFF0000FFFF;
	uint64_t mask3 = 0xFF00FF00FF00FF;
	uint64_t mask4 = 0xF0F0F0F0F0F0F0F;
	uint64_t mask5 = 0x3333333333333333;
	uint64_t mask6 = 0x5555555555555555;

	num = ((num >> 32) & mask1) | ((num << 32) & ~mask1);
	num = ((num >> 16) & mask2) | ((num << 16) & ~mask2);
	num = ((num >> 8) & mask3) | ((num << 8) & ~mask3);
	num = ((num >> 4) & mask4) | ((num << 4) & ~mask4);
	num = ((num >> 2) & mask5) | ((num << 2) & ~mask5);
	num = ((num >> 1) & mask6) | ((num << 1) & ~mask6);

	return num;
}


int main(){
	printf("%lX\n", reverse(0xABABEDEDABABEDED));
}