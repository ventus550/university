#include <iostream>
#include <vector>

using namespace std;

const vector<pair<int, string>> rzym = {
    {1000, "M"},
    {900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
    {90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"},
    {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
};

string bin2rom (int x) {
    int r = 0;
    string str = "";

    while(r < 13) {
        while(x - rzym[r].first >= 0) {
            str += rzym[r].second;
            x -= rzym[r].first;
        }
        r++;
    }
    return str;
}

bool isvalid(string str) {
    const string MAX = "3999";

    if(str.length() > 4) {
        clog << "!illegal size" << endl;
        return false;
    }


    bool test = true;
    for(int i = 0; i < str.length(); i++) {
        if(str[i] < '0' || str[i] > '9') {
            clog << "!illegal characters" << endl;
            return false;
        }

        if(test && str.length() == 4 && str[i] > MAX[i]) {
            clog << "!illegal size" << endl;
            return false;
        }
        if(test && str.length() == 4 && str[i] < MAX[i])
            test = false;
    }
}

int main(int argc, const char** argv)
{
    for(int i = 1; i < argc; i++) {
        if(isvalid(argv[i]))
            cout << bin2rom(stoi(argv[i])) << endl;
    }
    return 0;
}
