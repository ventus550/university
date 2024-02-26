#include <stdio.h>
#include <inttypes.h>


uint64_t SolveSub(uint64_t X, uint64_t Y) {
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


uint64_t test(uint64_t X, uint64_t Y) {
	uint64_t X1 = (X >> 8) & 0x00FF00FF00FF00FF;
	uint64_t Y1 = (Y >> 8) & 0x00FF00FF00FF00FF;
	uint64_t X2 = X & 0x00FF00FF00FF00FF;
	uint64_t Y2 = Y & 0x00FF00FF00FF00FF;

	return (SolveSub(X1, Y1) << 8) + SolveSub(X2, Y2);
}





uint64_t Solve(uint64_t X, uint64_t Y) {
	uint64_t X1 = X & 0xFF00FF00FF00FF00;
	uint64_t Y1 = Y & 0xFF00FF00FF00FF00;
	uint64_t X2 = X & 0x00FF00FF00FF00FF;
	uint64_t Y2 = Y & 0x00FF00FF00FF00FF;
	

	uint64_t sum1 = X1 + Y1; //!
	uint64_t XY1 = sum1 & 0xFF00FF00FF00FF00;
	uint64_t sum2 = X2 + Y2; //!
	uint64_t XY2 = sum2 & 0x00FF00FF00FF00FF;
	uint64_t XY = XY1 + XY2;

	printf("XY %lX\n", XY);
	

	//OF
	uint64_t XORxy = X ^ Y;
	uint64_t SameSign = ~XORxy;
	uint64_t XORsumx = XY ^ X;
	//Overflow detection
	uint64_t Calc1 = (SameSign & XORsumx) & 0x8080808080808080; //znaki operandw są takie same oraz znak sumy jest inny niż znak operandu
	//printf("Calc1 %lX\n", Calc1);
	uint64_t One = Calc1 >> 7;
	//printf("One %lX\n", One);
	uint64_t Calc2 = Calc1 - One;
	//printf("Calc2 %lX\n", Calc2);
	uint64_t OF = Calc2 + Calc1;
	//printf("OF %lX\n", OF);

	//min_max
	uint64_t Sx = 0x8080808080808080 & X;
	uint64_t Sx_shifted = Sx >> 7;
	uint64_t MIN_MAX = 0x7F7F7F7F7F7F7F7F + Sx_shifted;

	return (~OF & XY) + (OF & MIN_MAX);
}


// 0x00AA00BB00CC00DD
int main(){
	printf("Solve: %lX\n", Solve(0x00AA00800080007E, 0x0000007E00800010));
	printf("Test:  %lX\n",  test(0x00AA00800080007E, 0x0000007E00800010));
}