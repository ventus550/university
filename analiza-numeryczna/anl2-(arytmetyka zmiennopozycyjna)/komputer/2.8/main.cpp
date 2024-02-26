#include <iostream>
#include <math.h>

using namespace std;

double bad(double x) {return 4040.0*(sqrt(pow(x, 11)+1) - 1)/pow(x, 11);}
double good(double x) {
    return 4040.0/(sqrt(pow(x, 11)+1)+1);
}

void compare() {

    for(int i = 0; i <= 20; i++) {
        double x = 1.0/pow(10, i);
        cout << x << " --------" << endl;
        cout << "bad:" << bad(x) << endl;
        cout << "good:" << good(x) << endl << "--------" << endl;
    }
}



int main()
{
    compare();
    return 0;
}
