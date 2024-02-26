#include <iostream>
#include <math.h>


using namespace std;

//Z1
double z1(double x) {
    return 4040 * sqrt(pow(x, 11) + 1) / pow(x, 11);
}

//Z2
double z2_1(double x) {
    return 12120 * (x - sin(x)) / pow(x, 3);
}

float z2_2(float x) {
    return 12120 * (x - sin(x)) / pow(x, 3);
}

void calc2() {

    cout << "DOUBLE -------------" << endl;
    for(int i = 11; i <= 20; i++) {
        cout << z2_1(pow(10, -i)) << endl;
    }

    cout << "FLOAT -------------" << endl;
    for(int i = 11; i <= 20; i++) {
        cout << z2_2(pow(10, -i)) << endl;
    }

    cout << "--------------------" << endl;
}
//Z3

double rec(int n) {
    if(n == 0) {return 1.0;}
    if(n == 1) {return -1.0/7.0;}

    return 1.0/7.0 * (69 * rec(n-1) + 10 * rec(n-2));
}

void calc3() {
    for (int n = 2; n <= 50; n++) {
        cout << rec(n) << endl;
    }
    cout << "---------------" << endl;
}

//Z4
double integral(int n) {
    if(n == 0) {return log(2021.0/2020.0);}
    return 1.0/n - 2020*integral(n-1);
}

double integral_iter(int n)
{
    double result = (double)log(2021.0 / 2020.0);

    for(int i = 1; i <= n; i++)
    {
        result = 1.0/i - 2020.0 * result;
    }

    return result;
}

void calc4() {
    for (int i = 1; i <= 20; i++) {
        cout << integral_iter(i) << endl;
    }
}

//Z5
double series() {
    double l = 0.0;

    for(int k = 0; k < 19999; k++) {

        double tmp = 4.0/(2.0*k + 1);

        if(k % 2 == 0) {
            l += tmp;
        } else {
            l -= tmp;
        }

    }

    cout << l << endl;
}


int main()
{
    calc3();
    return 0;
}
