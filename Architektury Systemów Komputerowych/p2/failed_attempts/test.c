#include <stdio.h>
#include <inttypes.h>

uint64_t MassOF(uint64_t VX) {

	uint64_t SVX = VX >> 8;
	uint64_t mask = 0x00FF00FF00FF00FF;
	
	uint64_t A = SVX & mask;
	A += 0x0100010001000100;
	A -= 0x0001000100010001;

	return A & mask;
}


uint64_t MassMinMax(uint64_t V) {

	uint64_t mask = 0x0080008000800080;
	uint64_t max_mask = 0x007F007F007F007F;
	uint64_t B = V & mask;
	//printf("%lX\n", B);
	B = B >> 7;
	//printf("%lX\n", B);
	return max_mask + B;

}

uint64_t MassCalc(uint64_t V, uint64_t X) {

	uint64_t VX = V + X; //V,X są postaci 0 ele 0 ele ...
	printf("%lX\n", VX);
	uint64_t MOF = MassOF(VX);
	printf("%lX\n", MOF);
	return (MOF & VX) + (~MOF & MassMinMax(V));
}



// 0x00AA00BB00CC00DD
int main(){
	printf("%lX\n", MassCalc(0x00AA00BB00CC00FF, 0x0000000000000001));
}