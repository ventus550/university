#include <stdint.h>
#include <stdio.h>

void bin(uint32_t n) { 
    int binaryNum[32]; 
    int i = 0; 
    while (n > 0) { 
        binaryNum[i] = n % 2; 
        n = n / 2; 
        i++; 
    } 
    for (int j = i - 1; j >= 0; j--) {
		printf("%d", binaryNum[j]);
	}
	printf("\n");
}

uint32_t copy(uint32_t x, uint32_t i, uint32_t k) {
	uint32_t t = (1 << i) & x;
	x &= ~(1 << k);
	return x + ((t >> i) << k);
}


uint32_t speedcount(unsigned int n)
{
	n = n - ((n >> 1) & 0x55555555);
	n = (n & 0x33333333) + ((n >> 2) & 0x33333333);
	n = (n + (n >> 4)) & 0x0F0F0F0F;
	n = n + (n >> 8);
	n = n + (n >> 16);
	return n & 0x0000003F;
}

/*
uint32_t count(uint32_t n) {
	n = (n & 0x55555555) + ((n >>1) & 0x55555555); //dzieli na pojedyncze bity i dodaje je ze sobą
    n = (n & 0x33333333) + ((n >>2) & 0x33333333); //dzieli na pary bitów i dodaje je ze sobą
    n = (n & 0x0F0F0F0F) + ((n >>4) & 0x0F0F0F0F); //dzieli na czwórki bitów i dodaje je ze sobą
    n = (n & 0x00FF00FF) + ((n >>8) & 0x00FF00FF); //dzieli na ósemki bitów i dodaje je ze sobą
    n = (n & 0x0000FFFF) + ((n >>16) & 0x0000FFFF); //dzieli na szesnastki bitów i dodaje je ze sobą
	return n;
}
*/


uint32_t count(uint32_t n) {
	n = (n & 0x55555555) + ((n >>1) & 0x55555555); 
    n = (n & 0x33333333) + ((n >>2) & 0x33333333); 
    n = (n & 0x0F0F0F0F) + ((n >>4) & 0x0F0F0F0F); 
    n = (n & 0x00FF00FF) + ((n >>8) & 0x00FF00FF); 
    n = (n & 0x0000FFFF) + ((n >>16) & 0x0000FFFF);
	return n;
}


int main() {
	bin(121);
	bin(copy(121, 1, 0));

	printf("%d", count(0xFFFFFFF));
}