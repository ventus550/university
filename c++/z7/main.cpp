#include "wymierne.cpp"

using namespace obliczenia;
int main()
{
    wymierna w1(6, 2);
    wymierna w2 = w1;
    cout << w2 << endl;
    cout << w2.getLicz() << w2.getMian() << endl;
    cout << !w2 << endl;
    cout << -w2 << endl;
    cout << w1 + w2 + w2 << endl;
    cout << *(new wymierna(5)) << endl;
    cout << w1 * w2 << endl;
    cout << w1 / w2 << endl;
    wymierna w3(133, 74);
    cout << w3 << " " << (int)w3 << " " << (double)w3 << endl;

    //! wymierna w4(133, 0);
    wymierna w5(55555);
    //! w5 * w5;


    return 0;
}
