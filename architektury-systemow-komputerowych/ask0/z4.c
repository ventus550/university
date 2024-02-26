#include <stdint.h>
#include <stdio.h>

uint32_t a(uint32_t x, uint32_t y) { return x << y; }

uint32_t b(uint32_t x, uint32_t y) { return x >> y; }

uint32_t c(uint32_t x, uint32_t y) { return x - ((x >> y) << y); }

uint32_t d(uint32_t x, uint32_t y) { return (x + (1 << y) - 1) >> y; }


int main() {
    printf("%u\n", a(5, 2));
    printf("%u\n", b(5, 2));
    printf("%u\n", c(11, 2));
    printf("%u\n", d(8, 2));
}