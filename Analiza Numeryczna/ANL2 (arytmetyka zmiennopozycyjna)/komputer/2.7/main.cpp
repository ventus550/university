#include <iostream>
#include <math.h>
#include <iomanip>
using namespace std;
//a
double a_bad(double x) {return pow(x, 3) - sqrt(pow(x, 6) + 2020);}
double a_good(double x) {return 4040.0 / (sqrt(pow(x, 11) + 1) + 1);}

void a_compare() {
    for(int i = 1; i <= 20; i++) {
        double x = 2020 + pow(10, i);
        cout << x << " --------" << endl;
        cout << "bad:" << a_bad(x) << endl;
        cout << "good:" << a_good(x) << endl << "--------" << endl;
    }
}

//b
double fact(int n) {
    double res = 1.0;
    for(int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

double b_bad(double x) {return (cos(x) - 1 + pow(x,2) / 2.0) / pow(x, 4);}
double b_good(double x) {
    return 1.0/fact(4) - pow(x, 2)/fact(6) + pow(x, 4)/fact(8);
}

void b_compare() {
    for(int i = 0; i <= 20; i++) {
        double x = 1.0/pow(10, i);
        cout << x << " --------" << endl;
        cout << "bad:" << b_bad(x) << endl;
        cout << "good:" << b_good(x) << endl << "--------" << endl;
    }
}

//c
double log5(double x) {
    return log(x)/log(5);
}

float c_bad(float x) {return log5(x) - 6;}

float c_good(float x) {
    return log(x/pow(5, 6))/log(5);
}

void c_compare() {
    const float five = pow(5, 6);
    for(int i = 0; i <= 100; i++) {
        float x = five + 1.0/pow(10, i);
        cout << setprecision(30) << x << " --------" << endl;
        cout << "bad:" << setprecision(30) << c_bad(x) << endl;
        cout << "good:" << setprecision(30) << c_good(x) << endl << "--------" << endl;
    }
}




int main()
{
    c_compare();
    return 0;
}
