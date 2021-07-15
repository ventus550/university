#include <stdio.h>
#include <inttypes.h>

uint64_t Solve(uint64_t X, uint64_t Y) {
	uint64_t sum = X + Y; //!
	uint64_t XY = sum & 0x00FF00FF00FF00FF;

	//OF
	uint64_t XORxy = X ^ Y;
	uint64_t SameSign = ~XORxy;
	uint64_t XORsumx = XY ^ X;
	uint64_t Calc1 = (SameSign & XORsumx) & 0x0080008000800080;
	uint64_t Calc2 = Calc1 >> 7;
	uint64_t Calc3 = 0x0100010001000100 - Calc2;
	uint64_t OF = Calc3 & 0x00FF00FF00FF00FF;

	//min_max
	uint64_t Sx = 0x0080008000800080 & X;
	uint64_t Sx_shifted = Sx >> 7;
	uint64_t MIN_MAX = 0x007F007F007F007F + Sx_shifted;

	return (~OF & XY) + (OF & MIN_MAX);
}


// 0x00AA00BB00CC00DD
int main(){
	printf("%lX\n", Solve(0x00AA00800080007E, 0x0000007E00800010));
}