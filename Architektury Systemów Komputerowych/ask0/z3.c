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

uint32_t clear(uint32_t n, int k) { return n & ~(1<<k); }

uint32_t set(uint32_t n, int k) { return n | (1<<k); }

uint32_t toggle(uint32_t n, int k) { return n ^ (1<<k); }



int main() {
    bin(121);
    bin(clear(121, 0));
    bin(set(121, 1));
    bin(toggle(121, 0));
}