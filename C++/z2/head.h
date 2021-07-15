#ifndef HEAD_H_INCLUDED
#define HEAD_H_INCLUDED

class Wektor {
    void operator=(Wektor&) = delete;

    public:
        const double dx = 0, dy = 0;
        Wektor();
        Wektor(const double, const double);
        Wektor(const Wektor&);
};

class Punkt {


    public:
        const double x = 0, y = 0;
        void operator=(Punkt&) = delete;

        Punkt();
        Punkt(const double, const double);
        Punkt(const Punkt, const Wektor);
        Punkt(const Punkt&);
};

class Prosta {


    private:
        double A, B, C;

        void normalizuj();

    public:
        double getA();
        double getB();
        double getC();

        Prosta();

        Prosta(const Prosta&);

        Prosta(const Punkt, const Punkt);

        Prosta(const Wektor);

        Prosta(const double, const double, const double);

        Prosta(Prosta, const Wektor);

        bool czy_wektor_prostopadly(const Wektor);

        bool czy_wektor_rownolegly(const Wektor);

        bool czy_punkt_na_prostej(const Punkt);
};


#endif // HEAD_H_INCLUDED
