#include <stdio.h>
#include <inttypes.h>

uint64_t Solve(uint64_t X, uint64_t Y) {
	uint64_t sign_mask = 0x0080008000800080;
	uint64_t max_mask = 0x007F007F007F007F;
	uint64_t mask = 0x00FF00FF00FF00FF;
	uint64_t sum = X + Y;
	uint64_t XY = sum & mask;

	//OF
	uint64_t Sx = sign_mask & X;
	uint64_t Sy = sign_mask & Y;
	uint64_t Sxy = XY & sign_mask;
	uint64_t SameSign = ~(Sx ^ Sy); //interesuje nas tylko pierwszy bit
	uint64_t SumToOperandSign = Sxy ^ Sx;
	uint64_t Calc1 = SameSign & SumToOperandSign;
	uint64_t Calc2 = Calc1 >> 7;
	uint64_t Calc3 = 0x0100010001000100 - Calc2;
	uint64_t OF = Calc3 & mask;

	//min_max
	uint64_t Sx_shifted = Sx >> 7;
	uint64_t MIN_MAX = max_mask + Sx_shifted;

	return (~OF & XY) + (OF & MIN_MAX);
}


// 0x00AA00BB00CC00DD
int main(){
	printf("%lX\n", Solve(0x00AA00800080007E, 0x0000007E00800010));
}