#include<stdint.h>
#include<assert.h>
#include<stdbool.h>
#include<limits.h>

const int N = 32;

/*
**overflow** - występuje kiedy wynik działania jest zbyt duży 
(na minusie lub na plusie) w stosunku do tego na co pozwala 
reprezentacja.

**underflow** - kiedy wynik jest co do modułu zbyt mały żeby
mógł być zareprezentowany. Odnosi się głównie do liczb 
zmiennoprzecinkowych.
Nadmiar w dodawaniu może wystąpić tylko kiedy liczby są 
tego samego znaku. Można sprawdzić też, że wtedy wynik 
jest innego znaku.
*/

int32_t overflows(int32_t x, int32_t y){
    return ((x + y ^ x) & (x + y ^ y)) >> N - 1;
}

int main() {

    assert(overflows(INT32_MAX,1));
    assert(overflows(INT32_MIN,-1));
    assert(!overflows(4,3));

    return 0;
}