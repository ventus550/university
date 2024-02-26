#include <stdint.h>
#include <stdio.h>

void endian() {
	uint32_t x = (x >> 16) | (x << 16);
	x = ((x >> 8) & 0x00FF00FF) | ((x & 0x00FF00FF) << 8);
}

int main() {
	endian();
}