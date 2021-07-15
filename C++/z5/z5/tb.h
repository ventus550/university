#ifndef TB_H_INCLUDED
#define TB_H_INCLUDED
#include <iostream>

using namespace std;

class tab_bit
{
    typedef uint64_t slowo;        // komorka w tablicy
    static const int rozmiarSlowa = sizeof(slowo) * 8; // rozmiar slowa w bitach
    friend istream &operator>>(istream &, tab_bit &tb);
    friend ostream &operator<<(ostream &, const tab_bit &tb);
    class ref {
        public:
            slowo *s;
            int accessed;
            ref(slowo &);
            bool bRead(int);
            void bSet(int, bool);
            ref &operator=(const ref &);
            ref &operator=(const int &);
            operator bool() const;
    };

protected:
    int dl;     // liczba bitów
    slowo *tab; // tablica bitów
public:
    explicit tab_bit(int); // wyzerowana tablica bitow [0...rozm]
    explicit tab_bit(slowo); // tablica bitów [0...rozmiarSlowa]
    // zainicjalizowana wzorcem
    tab_bit(const tab_bit &);            // konstruktor kopiujący
    tab_bit(tab_bit &&);                 // konstruktor przenoszący
    tab_bit &operator=(const tab_bit &); // przypisanie kopiujące
    tab_bit &operator=(tab_bit &&);      // przypisanie przenoszące
    ~tab_bit();                            // destruktor
private:
    bool czytaj(int); // metoda pomocnicza do odczytu bitu
    bool pisz(int, bool); // metoda pomocnicza do zapisu bitu
public:
    bool operator[](int) const; // indeksowanie dla stałych tablic bitowych
    ref operator[](int);        // indeksowanie dla zwykłych tablic bitowych
    inline int rozmiar() const;  // rozmiar tablicy w bitach
public: // operatory bitowe: | i |=, & i &=, ^ i ^= oraz !
    tab_bit &operator|(tab_bit &);
    tab_bit &operator|=(tab_bit &);
    tab_bit &operator&(tab_bit &);
    tab_bit &operator&=(tab_bit &);
    tab_bit &operator^(tab_bit &);
    tab_bit &operator^=(tab_bit &);
    tab_bit &operator!();
};


#endif // TB_H_INCLUDED
