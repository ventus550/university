#include <iostream>
#include "definicje.cpp"

#define LOG(x) cout << x << endl;

int main()
{

    //! dla czytelnosci liczby sa do jednego miejsca po przecinku
    //! jest to jedynie sposob reprezentacji i nie wplywa na obliczenia
    wyrazenie *w1 = new dziel(
        new mnoz(
            new odejmij(
                new zmienna("x"),
                new liczba(1)
            ),
            new zmienna("x")
        ),
        new liczba(2)
    );
    LOG(w1->opis())



    wyrazenie *w2 = new dziel(
        new dodaj(
            new liczba(3),
            new liczba(5)
        ),
        new dodaj(
            new liczba(2),
            new mnoz(
                new zmienna("x"),
                new liczba(7)
            )
        )
    );
    LOG(w2->opis())


    wyrazenie *w3 = new odejmij(
        new dodaj(
            new liczba(2),
            new mnoz(
                new zmienna("x"),
                new liczba(7)
            )
        ),
        new dodaj(
            new mnoz(
                new zmienna("y"),
                new liczba(3)
            ),
            new liczba(5)
        )
    );
    LOG(w3->opis())


    wyrazenie *w4 = new dziel(
        new cosine(
            new mnoz(
                new dodaj(
                    new zmienna("x"),
                    new liczba(1)
                ),
                new zmienna("x")
            )
        ),
        new potega(
            new e(),
            new potega(
                new zmienna("x"),
                new liczba(2)
            )
        )
    );
    LOG(w4->opis())
    LOG("\n--------Obliczenia----------")



    //! przyjmuje ze y = 0
    for(int i = 0; i <= 100; i++) {
        zmienna::let("x", 0.01 * i);
        LOG("X := " + to_string(0.01 * i))
        LOG(w1->oblicz())
        LOG(w2->oblicz())
        LOG(w3->oblicz())
        LOG(w4->oblicz())
        LOG("------------")
    }



    return 0;
}







