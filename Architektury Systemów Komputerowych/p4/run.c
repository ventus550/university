//gcc -std=c99 run.c bitrev.s && ./a.out

#include <stdio.h>
#include <inttypes.h>


uint64_t bitrev(uint32_t);
//uint32_t rev(uint32_t);

int main() {
    uint32_t x = 0xD4FE8000;
    printf("%lX\n", bitrev(x));

    //uint32_t t = 0b11110000000000000000000000000001;
    //printf("%" PRIx64 "\n", rev(t));

    return 0;
}