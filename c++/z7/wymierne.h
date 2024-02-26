#ifndef WYMIERNE_H_INCLUDED
#define WYMIERNE_H_INCLUDED
#include <vector>
#include <iostream>

using namespace std;
namespace obliczenia {
    class GenericError {};
    class dzielenie_przez_0 : public GenericError {};
    class przekroczenie_zakresu : public GenericError {};



    class wymierna {
        private:
            int licz, mian;

            bool isdup(vector<int>, int) const;
        public:

            void normalizuj() throw(dzielenie_przez_0);

            string okres() const;

            wymierna(int, int);

            wymierna(int);

            void setLicz(int);
            void setMian(int);
            int getLicz();
            int getMian();
            int getSign();

            wymierna& operator-();

            wymierna& operator!();

            operator double() const;

            operator int() const;

            wymierna& operator*(wymierna &) throw(przekroczenie_zakresu);

            wymierna& operator/(wymierna &) throw(przekroczenie_zakresu);

            wymierna& operator+(wymierna &) throw(przekroczenie_zakresu);
            wymierna& operator-(wymierna &) throw(przekroczenie_zakresu);

            friend ostream& operator<< (ostream &, const wymierna &);


    };
}
#endif // WYMIERNE_H_INCLUDED
