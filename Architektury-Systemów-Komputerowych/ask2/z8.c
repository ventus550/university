
#include<stdint.h>


const int N = 32;

int sign(int32_t x){
    return -(x >> N-1 & 1) | -x >> N-1 & 1; // andowanie z 1 bo right shift uzupełnia jedynkami ujemne //tak naprawdę to  -(x >> N-1 & 1) | (-x >> N-1 & 1)
}

/*
* Jeśli jest zerem to obie strony są równe zero, więc alternatywa bitowa zwróci 0.
* Jeśli liczba jest dodatnia to lewa strona alternatywy to 0, bo MSB x to 0. Liczba 
przeciwna do x musi mieć MSB = 1 (działa, bo -INTN_MAX, mieści się w intN_t). Czyli 
prawą stronę możemy ustawić na MSB(-x).
* Jeśli liczba jest ujemna to chcemy zwrócić -1, czyli -MSB. Prawa strona alternatywy 
bitowej wtedy jest równa 1 (dla INTN_MIN), lub 0, ale nie wpływa to na wynik, gdzyż -1 
to same jedynki w kodzie uzupełnień do 2.
*/

int main() {

	printf("%I32d", sign(-123123));

    return 0;
}