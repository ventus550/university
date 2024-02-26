#include <iostream>
#include <cstdlib>
#include <math.h>


using namespace std;

double absolute(double x) {
    if(x >= 0) {return x;}
    else {return -x;}
}
double f(double x) {return x - 0.49;}
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
        cout << "n=" << i << endl << "m=" << res << "  e=" << absolute(0.49 - res) << "  ~e=" << diff/pow(2, i++ + 1)<< endl << "----------------" << endl;

    } while(i<15);
}

int main()
{
    bi(0, 1);
    return 0;
}
