#include <iostream>
#include <math.h>

using namespace std;

double f_bad(int k) {
    if(k == 1) {return 2.0;}

    const double a = pow(f_bad(k-1)/pow(2, k-1), 2);

    return pow(2, k-1)*sqrt(2 * (1 - sqrt(1 - a)));
}

double f_good(int k) {
    if(k == 1) {return 2.0;}

    const double a = pow(f_good(k-1)/pow(2.0, k-1), 2);

    return pow(2.0, k-1)*sqrt(2.0 * (a / (1 + sqrt(1 - a))));
}


int main()
{
    for(int i = 1; i <= 50; i++) {
        cout << "-----------" << endl;
        cout << f_bad(i) << endl;
        cout << f_good(i) << endl;
    }
    return 0;
}
