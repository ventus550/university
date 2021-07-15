#include <stdio.h>

long puzzle(char *s, char *d) {

	char *siter = s;
	while(1) {
		char *diter = d;
		while(1) {
			if (*diter == 0) {return siter - s;}
			if (*diter == *siter) {
				s++;
				break;
			}
			diter++;
		}
	}

}



int main() {

	return 0;
}