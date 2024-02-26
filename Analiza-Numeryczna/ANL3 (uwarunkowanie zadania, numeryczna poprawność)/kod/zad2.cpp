#include <iostream>
#include <math.h>
#include <iomanip>

void lepsze_korzenie(double a, double b, double c)
{
    double x1, x2;
    double sqrt_delta = sqrt(b*b - 4*a*c);

    if(sqrt_delta >= 0 && a != 0)
    {
        if(b <= 0)
            {
                x1 = (-b + sqrt_delta) / (2 * a);
            }
            else
            {
                x1 = (-b - sqrt_delta) / (2 * a);
            }

            if(x1 != 0)
            {
                x2 = c / (a * x1);
            }
            else
            {
                x2 = -b / a;
            }

            std::cout << std::fixed << std::setprecision(40) << "x1=" << x1 << std::endl;
            std::cout << std::fixed << std::setprecision(40) << "x2=" << x2 << std::endl;
    }
    else{

        std::cout << "err" <<  std::endl;
    }
}

void gorsze_korzenie(double a, double b, double c)
{
    double x1, x2;
    double sqrt_delta = sqrt(b*b - 4*a*c);

    if(sqrt_delta >= 0 && a != 0)
    {
        x1 = (-b + sqrt_delta) / (2 * a);
        x2 = (-b - sqrt_delta) / (2 * a);

        std::cout << std::fixed << std::setprecision(40) << "x1=" << x1 << std::endl;
        std::cout << std::fixed << std::setprecision(40) << "x2=" << x2 << std::endl;
    }
    else
    {
        std::cout << "err" << std::endl;
    }

}

int main()
{
    double a = 0.000000001;
    double b = 5;
    double c = 0.000000001;

    std::cout << "BETTER\n";
    lepsze_korzenie(a, b, c);

    std::cout << "\n\nWORSE\n";
    gorsze_korzenie(a, b, c);



    return 0;
}
