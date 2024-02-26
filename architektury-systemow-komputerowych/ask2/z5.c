
#include<stdint.h>


/*
floor(x * 2/4) = (x >> 1)
floor(x * 1/4) = (x >> 2)
zauważmy, że jeśli części ułamkowe (x * 2/4) i (x * 1/4) sumują się do 1
to musimy dodać jedynkę, czyli patrzymy na dwa ostatnie bity x.

Przypuśćmy, że oba te bity to jeden to mamy wtedy (i tylko wtedy):
111,1 + 11,11 = (111 + 11) + (0,1 + 0,11) = (111+11) + (1,1) = 111+11+1

więc musimy dodać jedynkę.
Do tego musimy napisać stosowny warunek, który doda ją tylko w takim przypadku:
(x & (x>>1) & 1)
*/

int32_t threefourths(int32_t x) {
	return (x >> 1) + (x >> 2) + (x & (x>>1) & 1);
}

int main() {

	printf("%I32d", threefourths(5));

    return 0;
}