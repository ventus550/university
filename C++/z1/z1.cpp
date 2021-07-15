#include <iostream> 
#include <vector>
#include <cmath>
#include <string>

using namespace std;

vector<int64_t> factors(int64_t num) {
    vector<int64_t> v;
    //cout << num << endl;

    if (num < 0) {
        v.push_back(-1);
    }

    int64_t d = 2;
    while (abs(num) != 1) {
        if (v.size() == 0 && d > sqrt(num)) {
            v.push_back(num);
            break;
        }
        while (num % d == 0) {
            //cout << num << " " << d << endl;
            num /= d;

            if (v.size() == 0 || v[v.size() - 1] != d)
                v.push_back(d);
        }

        d++;
    }
    
    

    return v;
}

int64_t toInt(string str) {
    int64_t sum = 0;
    int64_t sign = 1;
    int64_t multiplier;

    if (str[0] == '-') {
        multiplier = pow(10, str.length() - 2);
        sign = -1;
    }
    else {
        multiplier = pow(10, str.length() - 1);
    }

    if (str.length() > to_string(INT64_MIN).length())
        throw invalid_argument("Number is out of range");
    
    if (str.length() == to_string(INT64_MAX).length()) {

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
        if (str[i] == '-') {
            continue;
        }

        if ((str[i] >= '0' && str[i] <= '9') == false) {
            throw invalid_argument("String doesn't represent a number");
        }
        
        sum += multiplier * (str[i] - '0') * sign;
        //cout << sum << ";" << multiplier << ";" << endl;
        multiplier /= 10;
    }

    return sum;
}

int main(int argc, char** argv)
{   

    if (argc == 1) {
        cerr << "<INSTRUKCJA>" << "\n";
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