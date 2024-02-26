#include <cmath>
#include "tb.hpp"

using namespace std;

istream &operator>>( istream  &input, tab_bit &tb ) {
    string str;
    input >> str;
    int len = str.length();
    tab_bit tmp = tab_bit(len);
    for (int i = 0; i < len; i++)
    {
        if (str[i] == '1')
            tmp.pisz(i, 1);
        else if (str[i] == '0')
            tmp.pisz(i, 0);
        else
            throw new invalid_argument("Character does not represent a bit");
    }
    tb = tmp;
    return input;
}
ostream &operator<<(ostream &output, tab_bit &tb) {
    for (int i = 0; i < tb.dl; i++)
    {
        output << tb.czytaj(i);
    }
    return output;
}


tab_bit::ref::ref(slowo &s) {this->s = &s;}
tab_bit::ref::ref(slowo &s, int idx) {this->s = &s; this->accessed = idx;}

bool tab_bit::ref::bRead(int i) {
    if(i < 0 || i >= tab_bit::rozmiarSlowa)
        throw new out_of_range("Index out of range");

    int t[rozmiarSlowa] = {0};
    slowo tmp = *s;
    int j = 0;
    while(tmp != 0) {
        t[j] = tmp % 2;
        tmp /= 2;
        j++;
    }
    return t[i];
}

tab_bit::ref tab_bit::ref::bSet(int i, bool val) {
    //cout << "TEST:" << bRead(i) << " " << val << endl;
    if(bRead(i) && !val)
        *s -= pow(2, i);
    if(!bRead(i) && val)
        *s += pow(2, i);
    return *this;
}

tab_bit::ref::operator bool() {
    return this->bRead(this->accessed);
}

tab_bit::ref &tab_bit::ref::operator= (bool val) {
    bSet(this->accessed, val);
    return *this;
}

tab_bit::ref &tab_bit::ref::operator= (ref r) {
    bSet(this->accessed, r.bRead(r.accessed));
    return *this;
}

tab_bit::tab_bit (int rozm) {
    if(rozm < 0)
        throw new invalid_argument("Invalid size");

    this->dl = rozm;
    this->tab = new tab_bit::slowo[rozm / tab_bit::rozmiarSlowa + 1];
    for (int i = 0; i < rozmiar() / tab_bit::rozmiarSlowa + 1; i++)
    {
        this->tab[i] = 0;
    }
}
tab_bit::tab_bit (slowo tb) {
    this->dl = tab_bit::rozmiarSlowa;
    this->tab = new tab_bit::slowo[1];
    for (int i = 0; i < rozmiar() / tab_bit::rozmiarSlowa + 1; i++)
    {
        this->tab[i] = 0;
    }
}
tab_bit::tab_bit (const tab_bit &tb) {
    this->dl = tb.dl;
    this->tab = new slowo[rozmiar() / tab_bit::rozmiarSlowa + 1];
    for (int i = 0; i < rozmiar() / tab_bit::rozmiarSlowa + 1; i++)
    {
        this->tab[i] = tb.tab[i];
    }
}
tab_bit::tab_bit (tab_bit &&tb) : dl(move(tb.dl)), tab(move(tb.tab)){
    tb.tab = nullptr;
}
tab_bit &tab_bit::operator = (const tab_bit &tb) {
    if(this != &tb) {
        this->dl = tb.dl;
        this->tab = new slowo[rozmiar() / tab_bit::rozmiarSlowa + 1];
        for (int i = 0; i < rozmiar() / tab_bit::rozmiarSlowa + 1; i++)
        {
            this->tab[i] = tb.tab[i];
        }
    }
    return *this;


}
tab_bit &tab_bit::operator = (tab_bit &&tb) {
    dl = move(tb.dl);
    tab = move(tb.tab);
    tb.tab = nullptr;
    return *this;
}
tab_bit::~tab_bit () {
    delete[] this->tab;
}

bool tab_bit::czytaj (int i) const{
    if (i >= rozmiar() | i < 0)
        throw new out_of_range("Index out of range");

    int idxT = i / tab_bit::rozmiarSlowa;
    int idxS = i - idxT * tab_bit::rozmiarSlowa;
    ref r = ref(this->tab[idxT]);
    return r.bRead(idxS);
}

bool tab_bit::pisz (int i, bool b) {
    if (i >= rozmiar() | i < 0)
        throw new out_of_range("Index out of range");

    int idxT = i / tab_bit::rozmiarSlowa;
    int idxS = i - idxT * tab_bit::rozmiarSlowa;
    ref r = ref(this->tab[idxT]);
    r.bSet(idxS, b);
    this->tab[idxT]=*(r.s);
    return b;
}


bool tab_bit::operator[] (int i) const{
    if (i >= rozmiar() | i < 0)
        throw new out_of_range("Index out of range");


        cout << "Jendak dzialam!!!!" << endl;
       return czytaj(i);
}
tab_bit::ref tab_bit::operator[] (int i) {
    if (i >= rozmiar() | i < 0)
        throw new out_of_range("Index out of range");
    int idxT = i / tab_bit::rozmiarSlowa;
    int idxS = i - idxT * tab_bit::rozmiarSlowa;
    ref r = ref(this->tab[idxT], idxS);
    return r;

}

tab_bit &tab_bit::operator| (tab_bit &tb) {
    tab_bit* res = new tab_bit(max(this->dl, tb.dl));

    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            res->pisz(i, this->czytaj(i) || tb.czytaj(i));
        else {
            if(this->dl < tb.dl)
                res->pisz(i, tb.czytaj(i));
            else
                res->pisz(i, this->czytaj(i));
        }
    }
    return *res;
}

tab_bit &tab_bit::operator|= (tab_bit &tb) {

    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            this->pisz(i, this->czytaj(i) || tb.czytaj(i));
        else {
            if(this->dl < tb.dl)
                this->pisz(i, tb.czytaj(i));
            else
                this->pisz(i, this->czytaj(i));
        }
    }
    return *this;
}

tab_bit &tab_bit::operator& (tab_bit &tb) {
    tab_bit* res = new tab_bit(max(this->dl, tb.dl));

    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            res->pisz(i, this->czytaj(i) && tb.czytaj(i));
        else {
            res->pisz(i, 0);
        }
    }
    return *res;
}

tab_bit &tab_bit::operator&= (tab_bit &tb) {

    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            this->pisz(i, this->czytaj(i) && tb.czytaj(i));
        else {
            this->pisz(i, 0);
        }
    }
    return *this;
}

tab_bit &tab_bit::operator^  (tab_bit &tb) {
    tab_bit* res = new tab_bit(max(this->dl, tb.dl));

    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            res->pisz(i, this->czytaj(i) != tb.czytaj(i));
        else {
            if(this->dl < tb.dl)
                res->pisz(i, tb.czytaj(i) != 0);
            else
                res->pisz(i, this->czytaj(i) != 0);
        }
    }
    return *res;
}

tab_bit &tab_bit::operator^=  (tab_bit &tb) {
    for(int i = 0; i < max(this->dl, tb.dl); i++) {
        if(i < min(this->dl, tb.dl))
            this->pisz(i, this->czytaj(i) != tb.czytaj(i));
        else {
            if(this->dl < tb.dl)
                this->pisz(i, tb.czytaj(i) != 0);
            else
                this->pisz(i, this->czytaj(i) != 0);
        }
    }
    return *this;
}

tab_bit &tab_bit::operator! () {
    tab_bit* res = new tab_bit(this->dl);
    for(int i = 0; i < this->dl; i++)
        res->pisz(i, !(this->czytaj(i)));

    return *res;
}
