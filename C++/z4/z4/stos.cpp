#include <iostream>
#include <algorithm>
#include <utility>
#include "stos.h"

stos::stos(stos& s) {
    cerr << "~Copy constructor called" << endl;
    ile = s.ile;
    pojemnosc = s.pojemnosc;
    tablica = s.tablica;
}
stos& stos::operator= (stos& s) {
    cerr << "~Copy operator called" << endl;
    ile = s.ile;
    pojemnosc = s.pojemnosc;
    tablica = s.tablica;
    return *this;
}
stos::stos(stos&& s) : ile(move(s.ile)), pojemnosc(move(s.pojemnosc)), tablica(move(s.tablica)) {
    cerr << "~Move constructor called" << endl;
    s.tablica = nullptr;
}

stos& stos::operator= (stos&& s) {
    cerr << "~Move operator called" << endl;
    ile = move(s.ile);
    pojemnosc = move(s.pojemnosc);
    tablica = move(s.tablica);
    return *this;
}
stos::stos() : stos(1) {}
stos::stos(int cp) : pojemnosc(cp) {
    if(cp > 100)
      throw out_of_range("Stos jest pelny");
    tablica = new string[pojemnosc];
}
stos::stos(initializer_list<string> l){
    cerr << "~Initializer constructor called" << endl;
    pojemnosc = l.size();
    tablica = new string[pojemnosc];
    for(string str : l)
        wloz(str);
}


stos::~stos(){
    cerr << "~Destructor called" << endl;
    delete []tablica;
}


void stos::wloz(string str) {
    if(ile == 100 || ile == pojemnosc) {
        throw out_of_range("Stos jest pelny");
    } else {
        tablica[ile] = str;
        ile++;
    }


}
string stos::sciagnij() {
    if(ile == 0)
        return "";
    ile--;
    return tablica[ile];
}
string stos::sprawdz() {
    if(ile == 0)
        return "";
    return tablica[ile - 1];
}
int stos::rozmiar() {
    return ile;
}
stos stos::odwroc() {
    stos t(pojemnosc);
    int i = ile;

    while(i != 0)
        t.wloz(tablica[--i]);

    return t;
}
