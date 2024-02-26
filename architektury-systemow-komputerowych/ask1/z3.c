#include <stdint.h>
#include <stdio.h>

// a----
// bbbbb
// cdd--
struct A {
	int8_t a;
	void *b; //4B
	int8_t c;
	int16_t d;
};

// a----
// bbbbb
// c--dd
struct minA {
	void *b; //4B
	int16_t d;
	int8_t a;
	int8_t c;
};


// aa------
// bbbbbbbb	
// cccc----
struct B {
	uint16_t a;
	double b; //8B
	void *c; //4B
};

// bbbbbbbb
// ccccaa--
struct minB {
	double b; //8B
	void *c; //4B
	uint16_t a;
};



int main() {
	printf("%ld -> %ld\n", sizeof(struct A), sizeof(struct minA) );
	printf("%ld -> %ld\n", sizeof(struct B), sizeof(struct minB) );
}

