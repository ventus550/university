#include <stdint.h>
#include <stdio.h>

void hex(uint32_t decimalNumber) { printf("%X\n",decimalNumber); }

uint32_t convert(uint32_t x) {
	return (x>>24) | ((x>>8) & 0x0000ff00) | ((x<<8) & 0x00ff0000) | (x<<24);
}

int main() {
	uint32_t x = 0x12345678;
	hex(x);
	hex(convert(x));
}

