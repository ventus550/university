#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <chrono>

#define LOG(x) cout << x << endl;

using namespace std;

int64_t isprime(int64_t num) {
    uint64_t root;

    if (num == -1)
        return false;

    if (num < 0) {
        root = sqrt(-(num + 1)) + 1;
    } else
        root = sqrt(num);

    for(int64_t i = 2; i <= root; i++)
        if(num % i == 0)
            return false;
    return true;
}


vector<int64_t> factors(int64_t num) {
    vector<int64_t> v;
    if(num < 0)
        v.push_back(-1);

    if(isprime(num)) {
        v.push_back(abs(num));
        return v;
    }

    int64_t d = 2;
    while (num != 1 && num != -1) {

        while (num % d == 0) {
            num /= d;
            v.push_back(d);
        }
        d++;
    }
    return v;
}

int64_t ipow(const unsigned int p) {
    //wynik z standardowego pow() byl aproksymacyjny..

    int64_t res = 1;

    for (int i = 0; i < p; i++)
        res *= 10;

    return res;
}

int64_t toInt(string str) {
    int64_t sum = 0;
    int64_t sign = 1;
    int64_t multiplier;

    if ((str[0] == '0' && str.length() > 1) ||
        (str.length() > 2 && str[0] == '-' && str[1] == '0') ||
        (str.length() == 1 && str[0] == '-'))

        throw invalid_argument("String doesn't represent a number");


    if (str[0] == '-') {
        multiplier = ipow(str.length() - 2);
        sign = -1;
    }

    else {
        multiplier = ipow(str.length() - 1);
    }

    if (str.length() > to_string(INT64_MIN).length())
        throw invalid_argument("Number is out of range");

    if ((sign == 1 && str.length() == to_string(INT64_MAX).length()) ||
        (sign == -1 && str.length() == to_string(INT64_MIN).length())){

        string mxstring;
        if (sign == 1)
            mxstring = to_string(INT64_MAX);
        else
            mxstring = to_string(INT64_MIN);


        for (int i = 0; i < mxstring.length(); i++) {
            if (str[i] < mxstring[i])
                break;

            if (str[i] > mxstring[i])
                throw invalid_argument("Number is out of range");
        }

    }




    for (int i = 0; i < str.length(); i++) {
        if (str[i] == '-' && i == 0) {
            continue;
        }

        if ((str[i] >= '0' && str[i] <= '9') == false) {
            throw invalid_argument("String doesn't represent a number");
        }

        sum += multiplier * (str[i] - '0') * sign;
        multiplier /= 10;
    }

    return sum;
}

int main(int argc, char** argv) {

    if (argc == 1) {
        cerr << "Nalezy podac co najmniej jedna liczbe calkowita int64_t jako argument: \n <arg1> <arg2> <arg3> ..." << "\n";
    }

    for (int i = 1; i < argc; ++i) {
        vector<int64_t> f = factors(toInt(argv[i]));
        cout << argv[i] << " = ";
        cout << f[0];
        f.erase(f.begin(), f.begin() +1);

        for (int x : f)
            cout << " * " << x;
        cout << "\n";


    }
    return 0;
}
