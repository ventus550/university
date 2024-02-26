//gcc -std=c99 run.c bitrev.s && ./a.out

#include <stdio.h>
#include <inttypes.h>


uint64_t bitrev(uint64_t);
//uint32_t rev(uint32_t);

int main() {
	uint64_t x = 0b1111011110110011110101011001000111100110101000101100010010000000;
    printf("%" PRIx64 "\n", bitrev(x));

    //uint32_t t = 0b11110000000000000000000000000001;
    //printf("%" PRIx64 "\n", rev(t));

    return 0;
}