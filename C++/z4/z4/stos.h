#ifndef HEAD_H_INCLUDED
#define HEAD_H_INCLUDED

#define LOG(x) cout << x << endl;

using namespace std;

class stos {
    private:

        int ile = 0;
        int pojemnosc;
        string* tablica;


    public:


        stos(stos&);
        stos& operator= (stos&);
        stos(stos&& s);
        stos& operator= (stos&& s);
        stos();
        stos(int cp);
        stos(initializer_list<string>);

        ~stos();

        void wloz(string);
        string sciagnij();
        string sprawdz();
        int rozmiar();
        stos odwroc();

};
#endif // HEAD_H_INCLUDED
