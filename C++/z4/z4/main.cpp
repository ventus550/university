#include "stos.cpp"
#include <conio.h>
#include <cstdlib>

void print(stos s) {
    system("cls");
    LOG("Zawartosc stosu:");

    while(s.rozmiar() != 0)
        LOG(s.sciagnij());

    LOG("")
}

void add(stos& s) {
    LOG("")
    LOG("Podaj napis do wstawienia")
    string str;
    cin >> str;
    s.wloz(str);
}

void rem(stos& s) {
    LOG("")
    LOG("Zdjety element:")
    LOG(s.sciagnij())
}

void ssize(stos& s) {
    LOG("")
    LOG("Rozmiar stosu:")
    LOG(s.rozmiar())
}

void capacity() {
    LOG("")
    LOG("Pojemnosc stosu: 10")
}







int main()
{
    LOG("Testy dla konstruktorow")
    stos s = {"ala", "ma", "kota"};
    stos x(s);
    stos y;
    y = x;
    stos z = move(x);
    z = move(y);

    getch();
    stos* S = new stos(10);
    while (true) {
        system("cls");
        LOG("Prosze wybrac operacje na stosie:")
        LOG("1 := Wypisz stos")
        LOG("2 := Wstaw element na stos")
        LOG("3 := Usun element ze stosu")
        LOG("4 := Wypisz rozmiar stosu")
        LOG("5 := Pojemnosc stosu")
        LOG("else := End")

        switch(getch()) {

        case '1':
            print(*S);
            break;
        case '2':
            add(*S);
            break;
        case '3':
            rem(*S);
            break;
        case '4':
            ssize(*S);
            break;
        case '5':
            capacity();
            break;
        default:
            delete[] S;
            return 0;
            break;
        }

        LOG("")
        LOG("Wcisnij dowolny klawisz by kontynuowac")
        getch();
    }
    return 0;
}
