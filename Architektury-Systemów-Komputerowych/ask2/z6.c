
#include<stdint.h>
#include<stdio.h>


/*
Rozwiązanie takie unika problemu przepełnienia przez przesunięcie o jedno miejsce w prawo x i y.
Zauważmy jednak, że przy takim przesunięciu gdy odejmujemy od x y, a y ma na najmniej znaczacym bicie 1, a x 0 to pomijamy to w naszych wyliczeniach.
Musimy tą stratę odjąc od wyniku i za to odpowiada ~x & y & 1, które sprawdza czy powinniśmy odjąć 1 od wyniku czy nie. >> 31 wydobywa bit znaku i sprawdza czy odejmowanie dało wynik dodatni czy ujemny.
Ostatecznie program zwraca -1 gdy y>x i 0 wpp.

*/

const int N = 32;

int32_t compare(int32_t x, int32_t y) {
	return (((x >> 1) - (y >> 1) - (~x & y & 1)) >> N-1);
}

int main() {

	printf("%I32d", compare(-123123, 5));

    return 0;
}