//gcc depuzzled.c  && ./a.out

#include <stdio.h>
#include <inttypes.h>

//n - licznik, d - mianownik
uint32_t puzzle3(uint32_t n, uint32_t d){
	uint64_t num = n;
	uint64_t den = (uint64_t)d << 32;
	uint32_t edx = 32;
	uint32_t mask = 0x80000000;
	uint32_t result = 0;
	
	
	while(edx) {
        num *= 2;
		if(num >= den){
			result |= mask;
			num = num - den;
		}
		mask >>= 1;
		edx--;
	}
    return result;
}

int main() {
    printf("%d\n", puzzle3(1,1)); //1
    printf("%d\n", puzzle3(1,2)); //0
    printf("%d\n", puzzle3(2,1)); //2
    printf("%d\n", puzzle3(4,2)); //2
    printf("%d\n", puzzle3(8,4)); //2
    printf("%d\n", puzzle3(5,2)); //2
    printf("%d\n", puzzle3(7,2)); //3
    return 0;
}