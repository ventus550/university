#include "tb.cpp"
#include <conio.h>

using namespace std;

int main() {

    tab_bit t(46); // tablica 46-bitowa (zainicjalizowana zerami)
    tab_bit u(45ull); // tablica 64-bitowa (sizeof(uint64_t)*8)
    tab_bit v(t); // tablica 46-bitowa (skopiowana z t)
    v[0] = 1; // ustawienie bitu 0-go bitu na 1
    t[45] = true; // ustawienie bitu 45-go bitu na 1
    bool b = v[1]; // odczytanie bitu 1-go
    u[63] = 1;
    u[45] = u[46] = u[63]; // przepisanie bitu 63-go do bitow 45-go i 46-go
    cout << t << endl << v << endl << u << endl << b << endl;

    getch();
    system("cls");


    //operatory bitowe
    cout << "Podaj dwie dowolne tablice binane (przykladowy format: 101010)" << endl;
    tab_bit T1(0), T2(0), test(0);
    cin >> T1 >> T2;

    cout << T1 << " " << T2 << endl;

    test = T1 | T2;
    cout <<"Alternatywa podanych tablic: " << test << endl;

    test = T1 & T2;
    cout <<"Koniunkcja podanych tablic: " << test << endl;

    test = T1 ^ T2;
    cout <<"Roznica symetryczna podanych tablic: " << test << endl;

    cout <<"Negacja pierwszej tablicy: " << !T1 << endl;







    return 0;
}
