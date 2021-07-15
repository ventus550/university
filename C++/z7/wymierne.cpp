#include <iostream>
#include <cmath>
#include <algorithm>
#include "wymierne.h"

using namespace std;




bool obliczenia::wymierna::isdup(vector<int> v, int val) const{
    int k = 0;
    for(int i = 0; i < v.size(); i++) {
        if(v[i] == val)
            k++;
    }

    return k >= 2;
}

void obliczenia::wymierna::normalizuj() throw(dzielenie_przez_0){
    if(this->mian == 0)
        throw new dzielenie_przez_0;
    if(this->licz == 0)
        return;

    int &l = this->licz;
    int &m = this->mian;

    int sign = (l * m) / abs(l * m);
    l = abs(l);
    m = abs(m);

    int i = 2;
    while (i <= l && i <= m) {
        if (l % i == 0 && m % i == 0) {
            l /= i;
            m /= i;
        } else {
            i++;
        }
    }
    l *= sign;
}

string obliczenia::wymierna::okres() const{
    string str = "";
    vector<int> v;
    vector<int> rs;


    int r = this->licz, m = this->mian;
    do {
        v.push_back(r / m);
        r = r % m;
        if(v.size() > 1)
            rs.push_back(r);
        r *= 10;
    } while(r != 0 && !isdup(rs, r % m));

    str += to_string(v[0]);
    if(v.size() == 1)
        return str;

    str += ".";
    for(int i = 1; i < v.size() - 1; i++) {
        if(rs[i-1] == rs[rs.size()-1])
            str += "(";
        str += to_string(v[i]);
    }
    if(rs[rs.size() - 1] == 0)
        return str + to_string(v[v.size()-1]);
    return str + ")";
}


obliczenia::wymierna::wymierna(int l, int m){
    this->licz = l;
    this->mian = m;
    normalizuj();
}

obliczenia::wymierna::wymierna(int n) : wymierna(n, 1) {}

void obliczenia::wymierna::setLicz(int l) {this->licz = l; normalizuj();}
void obliczenia::wymierna::setMian(int m) {this->mian = m; normalizuj();}
int obliczenia::wymierna::getLicz() {return this->licz;}
int obliczenia::wymierna::getMian() {return this->mian;}
int obliczenia::wymierna::getSign() {return this->licz/abs(this->licz);}

obliczenia::wymierna &obliczenia::wymierna::operator-() {
    wymierna *w = new wymierna(this->licz, this->mian);
    w->licz *= -1;
    return *w;
}

obliczenia::wymierna &obliczenia::wymierna::operator!() {
    wymierna *w = new wymierna(this->mian, this->licz);
    return *w;
}

obliczenia::wymierna::operator double() const {return (1.0 * licz) / mian;}

obliczenia::wymierna::operator int() const {return floor((double)*this);}

obliczenia::wymierna& obliczenia::wymierna::operator*(wymierna &w) throw(przekroczenie_zakresu){
    if(((to_string(this->mian) + to_string(w.mian)).length() >= 10) ||
        (to_string(this->licz) + to_string(w.licz)).length() >= 10)
        throw new przekroczenie_zakresu;
    wymierna *wnew = new wymierna(this->licz * w.licz, this->mian * w.mian);
    normalizuj();
    return *wnew;
}

obliczenia::wymierna& obliczenia::wymierna::operator/(wymierna &w) throw(przekroczenie_zakresu){
    if(((to_string(this->mian) + to_string(w.licz)).length() >= 10) ||
        (to_string(this->licz) + to_string(w.mian)).length() >= 10)
        throw new przekroczenie_zakresu;

    wymierna *wnew = new wymierna(this->licz * w.mian, this->mian * w.licz);
    normalizuj();
    return *wnew;
}

obliczenia::wymierna& obliczenia::wymierna::operator+(wymierna &w) throw(przekroczenie_zakresu){
    if((max(to_string(this->mian).length(), to_string(w.mian).length()) >= 9) ||
        (this->getSign()*w.getSign() > 0 && max(to_string(this->mian).length(), to_string(w.mian).length()) >= 9))
        throw new przekroczenie_zakresu;

    wymierna *wnew = new wymierna((this->licz * w.mian) + (this->mian * w.licz), this->mian * w.mian);
    normalizuj();
    return *wnew;
}

obliczenia::wymierna& obliczenia::wymierna::operator-(wymierna &w) throw(przekroczenie_zakresu){
    if((max(to_string(this->mian).length(), to_string(w.mian).length()) >= 9) ||
        (this->getSign()*w.getSign() > 0 && max(to_string(this->mian).length(), to_string(w.mian).length()) >= 9))
        throw new przekroczenie_zakresu;

    wymierna *wnew = new wymierna((this->licz * w.mian) - (this->mian * w.licz), this->mian * w.mian);
    normalizuj();
    return *wnew;

}

ostream &operator<<(ostream &wyj, obliczenia::wymierna &w) {
    wyj << w.okres();
    return wyj;
}

