
#include<stdint.h>
#include<stdio.h>


/*
Wiemy, że   b ? x : -x  <=>  b * x + !b * -x           (nie wolno nam mnożyć :c)

b := x >> N-1

Czyli mnożenia możemy przedstawić w następujący sposób:
(b & x) + (~b & -x)

*/

const int N = 32;

int32_t aabs(int32_t x) {
	int32_t b = x >> N-1;
	return (b & -x) + (~b & x);
}

int main() {

	printf("%d", aabs(-22));

    return 0;
}