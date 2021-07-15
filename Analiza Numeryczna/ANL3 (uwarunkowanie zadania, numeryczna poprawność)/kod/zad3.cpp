// Example program
#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>

using namespace std;

double cardano_worse(double r, double q)
{
    return pow(r-sqrt(pow(q,3.0)+pow(r,2.0)),1.0/3.0);
}

double cardano_better(double r, double q)
{

    double a = r + sqrt(pow(q, 3) + pow(r, 2));
    return (2*r)/(pow(pow(a, 2), 1.0/3.0) + pow(q, 2)/pow(pow(a, 2), 1.0/3.0) + q);
}


int main()
{
    cout << fixed << setprecision(30) << cardano_worse(pow(10.0,4.0),pow(10.0,-4.0)) << endl;
    cout << fixed << setprecision(30) << cardano_better(pow(10.0,4.0),pow(10.0,-4.0)) << endl;
}
