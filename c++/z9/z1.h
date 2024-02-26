#ifndef Z1_H_INCLUDED
#define Z1_H_INCLUDED

#include <iostream>
#include <fstream>

using namespace std;



istream &clearline(istream &in);

class ignore {
    int val;
    friend istream& operator>>(istream &in, const ignore &ig);
    public:
        ignore(int v) : val(v) {}
};

inline ostream& comma(ostream &os);

inline ostream& colon(ostream &os);

class index {
    int x, w;
    friend ostream& operator<<(ostream &os, const index &ix);
    public:
        index(int x, int w) : x(x), w(w) {}
};

#endif // Z1_H_INCLUDED
