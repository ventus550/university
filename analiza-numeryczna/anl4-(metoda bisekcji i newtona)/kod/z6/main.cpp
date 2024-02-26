#include <iostream>
#include <cstdlib>
#include <math.h>
#include <iomanip>


using namespace std;

double Newton(double x0, double a, int n) {
    if(n == 0) {return x0;}
    const double prev = Newton(x0, a, n-1);
    return (3.0*prev - a*pow(prev, 3))*0.5;
}

void TestNewton(double x0, double a) {
    cout << "Testing for x0=" << x0 << " a=" << a << endl;
    for(int i = 0; i < 10; i++) {
        cout << "n=" << i << "   " << Newton(x0, a, i) << endl;
    }

    cout << "Expected: " << 1/sqrt(a) << endl << "-------------------------" << endl;
}


int main()
{
    TestNewton(0.2345, 0.2345);
    TestNewton(0.5, 10000);
    TestNewton(100000, 0.2345);
    TestNewton(1.01, 0.99);

    return 0;
}
