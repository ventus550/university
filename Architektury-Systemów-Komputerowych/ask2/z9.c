
#include<stdint.h>
#include<stdio.h>


int32_t odd_ones_suck(uint32_t x)
{
    x = (x & 0x55555555) + ((x >> 1) & 0x55555555);
    x = (x & 0x33333333) + ((x >> 2) & 0x33333333);
    x = (x & 0x0F0F0F0F) + ((x >> 4) & 0x0F0F0F0F);
    x = (x & 0x00FF00FF) + ((x >> 8) & 0x00FF00FF);
    x = (x & 0x0000FFFF) + ((x >> 16) & 0x0000FFFF);
    
    return (x & 1);
}

int32_t odd_ones(uint32_t x)
{
    x ^= x >> 1;
    x ^= x >> 2;
    x ^= x >> 4;
    x ^= x >> 8;
    x ^= x >> 16;
    return x & 1;
}

int main() {

	//printf("%I32d\n", abs(-123123));
    
    int32_t y = INT32_MIN-1;

    int32_t x = INT32_MIN;
    printf("%d\n",  (x-1) < 0); //1
    printf("%d\n",  (INT32_MIN-1) < 0); //0

    return 0;
}