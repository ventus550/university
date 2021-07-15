#include<iostream>
#include<cstdlib>
#include<cmath>

using namespace std;

double f(double x) {
    return pow(x, 2) - 2.0 * cos( 3.0 * x + 1.0);
}

bool test(bool pred, bool test) {
    if(pred) {return test;}
    return !test;
}

void bi(double a, double b) {

    const double e = pow(10, -5), diff = b-a;
    bool pred = f(b) >= 0;

    double res = 0;
    int i = 0;
    do {
        res = (a+b)/2.0;
        if(test(pred, f(res) > 0)) {
            b = res;
        } else {
            a = res;
        }

    } while(diff/pow(2, i++ + 1) > e);
    cout << res << endl;
}


int main() {

    bi(0, 1);
    bi(-1, 0);

    return 0;
}
