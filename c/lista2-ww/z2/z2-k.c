#include <stdio.h>
#include <assert.h>

#define MODULUS 4294967295

typedef unsigned char bool;

unsigned long Catalan(unsigned short n);
unsigned long CatalanMem(unsigned short n);

struct mem_entry {
    unsigned long value;
    bool valid;
};

struct mem_entry results[50];

int main()
{
    // Inicjalizacja liczba Catalana dla n = 0 i 1
    results[0].value = 1;
    results[0].valid = 1;
    results[1].value = 1;
    results[1].valid = 1;

    // Wartości liczb Catalana z Wikipedii
    unsigned long catalan_values[] = {1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440,
     9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452};


    unsigned short n, how_many = 30;
    unsigned long catalan_n; // Na 20-tym elemencie kończy się zakres unsigned long


// Obliczanie bez spamiętywania
    // for (unsigned short i = 0; i < how_many; i++)
    // {
        // catalan_n = Catalan(i);
        // printf("%d: %lu\n", i, catalan_n);
    // }

// Obliczanie ze spamiętywaniem
    for (unsigned short i = 0; i < how_many; i++)
        {
            catalan_n = CatalanMem(i);
            printf("%d: %lu\n", i, catalan_n);
        }

// Testowanie obu funkcji za pomocą asercji
    printf("TESTING...\n");
    for (int i = 0; i < 20; i++)
    {
        printf("Test %d: ", i);
        assert(Catalan(i) == catalan_values[i]);
        assert(CatalanMem(i) == catalan_values[i]);
        printf("passed\n");
    }
    printf("TESTS PASSED!\n");

}


// Definicje funkcji

unsigned long Catalan(unsigned short n)
{
    unsigned long result = 0;

    if (n <= 1) return 1;

    for (unsigned short i = 0; i < n; i++)
    {
        result += Catalan(i)*Catalan(n-i-1);
    }
    return result % MODULUS;
}

unsigned long CatalanMem(unsigned short n)
{
    unsigned long result = 0;

    if (n <= 1) return 1;

    for (unsigned short i = 0; i < n; i++)
    {
        // Jeśli wartości dla danych i są zapamiętane, to używamy ich do obliczenia następnej liczby Catalana,
        // jeśli nie, to liczymy je wprost z definicji
        if (results[i].valid && results[n-i-1].valid) result += results[i].value*results[n-i-1].value;
        else if(results[i].valid) result += results[i].value*Catalan(n-i-1);
        else result += Catalan(i)*Catalan(n-i-1);
    }

    // Przypisanie odpowiednich wartości do tablicy struktur
    results[n].value = result;
    results[n].valid = 1;

    return result % MODULUS;

}
