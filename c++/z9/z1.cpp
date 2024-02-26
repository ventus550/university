#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include "z1.h"

using namespace std;



istream &clearline(istream &in)
{
    while(in && in.get() != '\n'){}
    return in;
}


istream& operator>>(istream &in, const ignore &ig){
    int k = 0;
    while(in && in.get() != '\n' && k < ig.val - 1){ k++; }

    return in;
}


inline ostream& comma(ostream &os) {
    return os << ", ";
}

inline ostream& colon(ostream &os) {
    return os << ": ";
}


ostream& operator<<(ostream &os, const index &ix){
    string xstr = to_string(ix.x), res = "";

    int k = 0;
    while(k < xstr.length() && k < ix.w) {
        res += xstr[k];
        k++;
    }

    while(k < ix.w) {
        res = " " + res;
        k++;
    }
    res = "[" + res + "]";

    return os << res;
}


void test(int rows) {
    vector<pair<string, int>> v;

    for(int i = 0; i < rows; i++) {
        string s;
        getline(cin, s);
        v.push_back(make_pair(s, i));
    }
    sort(v.begin(), v.end());

    for(pair<string, int> p : v) {
        cout << index(p.second, 2) << " " << p.first << endl;
    }
}



int main()
{
    cout << "Hello" << comma << "world!" << colon << index(123, 4) << colon << index(123, 2) << "end" << endl << endl;
    cout << "Ignore(5) test" << endl;

    string ig;
    cin >> ignore(5) >> ig;
    cout << ig << endl << endl;

    cout << "Procedura testowa(12)" << endl;
    test(12);

    return 0;
}
