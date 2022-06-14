#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define MODULUS 200000000

//4294967295
typedef unsigned char bool;
struct mem_entry {
    unsigned long value;
    bool valid;
};

struct mem_entry memory[MODULUS];


unsigned long Catalan(unsigned short n) {
    if(n == 0)
        return 1;

    unsigned long sum = 0;
    for(int i = 0; i < n; i++)
        sum += Catalan(i) * Catalan(n - 1 - i);

    return sum % MODULUS;
}

unsigned long CatalanMem(unsigned short n) {
    if(n == 0)
        return 1;
    if(memory[n].valid == 1)
        return memory[n].value;

    unsigned long sum = 0;
    for(int i = 0; i < n; i++)
        sum += CatalanMem(i) * CatalanMem(n - 1 - i);

    sum %= MODULUS;
    memory[n].value = sum;
    memory[n].valid = 1;
    return sum;
}

int main()
{
    for(int i = 0; i < 200; i++)
        //printf("%d\n", CatalanMem(i));
        memory[i].valid;


    //-------------testy----------------------
    unsigned long catalan_values[] = {1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440,
     9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452};

    printf("Running tests\n");
    for (int i = 0; i <= 15; i++)
    {
        printf("C%d: ", i);
        assert(Catalan(i) == catalan_values[i]);
        assert(CatalanMem(i) == catalan_values[i]);
        printf("passed\n");

    }
    printf("End of testing");




    return 0;
}
