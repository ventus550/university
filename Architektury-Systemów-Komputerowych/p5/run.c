//gcc -std=c99 run.c bitrev.s && ./a.out

#include <stdio.h>
#include <inttypes.h>


int bitrev(uint64_t);
//uint32_t rev(uint32_t);

int main() {
    uint64_t x = 0x0f0f0f0f0f0f0f0f;
    uint64_t y = 0x9e25fdcb4df5ab60;
    printf("%d == %d\n", bitrev(x), x % 17);
    printf("%d == %d\n", bitrev(y), y % 17);
    return 0;
}