#include <stdio.h>
#include <inttypes.h>

uint64_t MassOF(uint64_t X, uint64_t Y) {

	uint64_t sign_mask = 0x0080008000800080;
	uint64_t Sx = sign_mask & X;
	printf("Sx %lX\n", Sx);
	uint64_t Sy = sign_mask & Y;
	printf("Sy %lX\n", Sy);

	uint64_t XY = X + Y;
	printf("XY %lX\n", XY);
	uint64_t Sxy1 = XY & sign_mask;
	printf("Sxy1 %lX\n", Sxy1);

	uint64_t SS = ~(Sx ^ Sy);
	printf("SS %lX\n", SS);

	SS = SS & (Sxy1 ^ Sx);
	printf("Sxy1 ^ Sx %lX\n", Sxy1 ^ Sx);
	SS = SS >> 7 ;
	SS = 0x0100010001000100 - SS;
	printf("- %lX\n", Sxy1 ^ Sx);
	return SS & 0x00FF00FF00FF00FF; 
}


uint64_t MassMinMax(uint64_t V) {

	uint64_t mask = 0x0080008000800080;
	uint64_t max_mask = 0x007F007F007F007F;
	uint64_t B = V & mask;
	//printf("%lX\n", B);
	B = B >> 7;
	//printf("%lX\n", B);
	//printf("max_mask + B %lX\n", max_mask + B);
	return max_mask + B;

}

uint64_t MassCalc(uint64_t X, uint64_t Y) {
	uint64_t mask = 0x00FF00FF00FF00FF;

	uint64_t VX = X + Y; //V,X są postaci 0 ele 0 ele ...
	VX = VX & mask;
	//printf("%lX\n", VX);
	uint64_t MOF = MassOF(X, Y);
	printf("MOF %lX\n", MOF);
	printf("MMM %lX\n", MassMinMax(X));
	printf("~MOF & VX %lX\n", ~MOF & VX);
	return (~MOF & VX) + (MOF & MassMinMax(X));
}



// 0x00AA00BB00CC00DD
int main(){
	printf("%lX\n", MassCalc(0x00AA00800080007E, 0x0000007E00800010));
}