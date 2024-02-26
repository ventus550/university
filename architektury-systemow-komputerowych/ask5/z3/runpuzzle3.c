//gcc -std=c99 runpuzzle3.c puzzle3.s && ./a.out


#include <stdio.h>
#include <inttypes.h>

int32_t puzzle3(uint32_t, int32_t);

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