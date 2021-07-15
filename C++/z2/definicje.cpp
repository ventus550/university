#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <time.h>
#include<conio.h>
#include "head.h"

#define LOG(x) cout << x << endl;
using namespace std;

Wektor::Wektor() = default;
Wektor::Wektor(const double a, const double b) : dx(a), dy(b) {};
Wektor::Wektor(const Wektor& w) : dx(w.dx), dy(w.dy) {};

Punkt::Punkt() = default;
Punkt::Punkt(const double a, const double b) : x(a), y(b) {};
Punkt::Punkt(const Punkt p, const Wektor w) : x(p.x + w.dx), y(p.y + w.dy) {};
Punkt::Punkt(const Punkt& p) : x(p.x), y(p.y) {};

void Prosta::normalizuj() {
    double x = sqrt(A*A + B*B);
    A /= x;
    B /= x;
    C /= x;
}

double Prosta::getA() {return A;};
double Prosta::getB() {return B;};
double Prosta::getC() {return C;};

Prosta::Prosta() = default;

Prosta::Prosta(const Punkt p, const Punkt q) {
    if (p.x == q.x && p.y == q.y)
        throw invalid_argument("nie mozna jednoznacznie utworzyc prostej");
    if (p.x == q.x) {
        A = 1;
        B = 0;
        C = -p.x;
    } else {
        A = (q.y - p.y) / (q.x - p.x);
        B = -1;
        C = -A*p.x + p.y;
    }



    normalizuj();
}

Prosta::Prosta(const Wektor w) {
    if(w.dx == 0 && w.dy == 0)
        throw invalid_argument("nie mozna jednoznacznie utworzyc prostej");

    if(w.dx == 0) {
        A = 0;
        B = -1;
        C = w.dy;
    }
    if(w.dy == 0) {
        A = 1;
        B = 0;
        C = -w.dy;
    }

    if(w.dx != 0 && w.dy != 0) {
        A = -w.dy / w.dx;
        B = -1;
        C = w.dx + w.dy;
    }

    normalizuj();

}

Prosta::Prosta(const double a, const double b, const double c) {
    if(a == 0 && b == 0)
        throw invalid_argument("nie można jednoznacznie utworzyć prostej");

    A = a;
    B = b;
    C = c;
    normalizuj();
}

Prosta::Prosta(Prosta pr, const Wektor w) {
    A = pr.getA();
    B = pr.getB();
    C = pr.getC() - (A * w.dx) - (B * w.dy);
    normalizuj();

}

bool Prosta::czy_wektor_prostopadly(const Wektor w) {
    Prosta pr(w);

    if(pr.getA() == A)
        return true;
    return false;
}

bool Prosta::czy_wektor_rownolegly(const Wektor w) {
    Prosta pr;
    if(w.dx != 0)
        pr = Prosta(Punkt(0,0), Punkt(w.dx, w.dy));
    else {
        pr = Prosta(1, 0, -w.dy);
    }

    if(pr.getA() == A)
        return true;
    return false;
}

bool Prosta::czy_punkt_na_prostej(const Punkt p) {
    //wynik jest aproksymacyjny stad zaokraglenie int()
    if(int(A*p.x + B*p.y + C) == 0)
        return true;
    return false;

}

bool czy_proste_rownolegle(Prosta p1, Prosta p2) {
    if(p1.getA() == p2.getA())
        return true;
    return false;
}

bool czy_proste_prostopadle(Prosta p1, Prosta p2) {
    if(p1.getA() == -p2.getA())
        return true;
    return false;
}

Punkt punkt_przeciecia_prostych(Prosta p1, Prosta p2) {
    const double
    A1 = p1.getA(),
    A2 = p2.getA(),
    B1 = p1.getB(),
    B2 = p2.getB(),
    C1 = p1.getC(),
    C2 = p2.getC();

    if(A1 == A2)
        throw invalid_argument("Proste nie moga byc rownolegle");

    double x = (B1*C2 - B2*C1) / (A1*B2 - A2*B1);
    double y = (A2*C1 - A1*C2) / (A1*B2 - A2*B1);

    return Punkt(x, y);
}


//------------------------------TESTY---------------------------------------------
void normalizacja_test(Prosta pr) {
    cout << pr.getA() << " " << pr.getB() << " " << pr.getC() << "   (A^2 + B^2) = " << pow(pr.getA(), 2) + pow(pr.getB(), 2) << endl;
}

string getABC(Prosta pr) {
    return "(A: " + to_string(pr.getA()) + " " + "B: " + to_string(pr.getB()) + " " + "C: " + to_string(pr.getC()) + ")";
}
int rnd() {
    return (rand() % 11) - 5;
}
void testy() {
    srand (time(NULL));

    //----
    Wektor w(rnd(), rnd());
    LOG("Prosta w oparciu o wektor(" << w.dx << ", " << w.dy << ") ======> prosta1:" + getABC(Prosta(w)));

    Prosta pr1(w);
    LOG("czy wektor prostopadly? " << pr1.czy_wektor_prostopadly(w));
    LOG("czy wektor rownolegly? " << pr1.czy_wektor_rownolegly(w));
    LOG(endl);



    //----
    Punkt p(rnd(), rnd());
    Punkt q(rnd(), rnd());
    LOG("Prosta w oparciu o punkty(" << p.x << ", " << p.y << ")(" << q.x << ", " << q.y << ") ======> prosta2:" + getABC(Prosta(p, q)));

    Prosta pr2(p , q);
    LOG("czy punkt1 na prostej? " << pr2.czy_punkt_na_prostej(p));
    LOG("czy punkt2 na prostej? " << pr2.czy_punkt_na_prostej(q));
    LOG(endl);

    //----
    LOG("czy_proste_prostopadle(prosta1, prosta2)? " << czy_proste_prostopadle(Prosta(w), Prosta(p,q)));
    LOG("czy_proste_rownolegle(prosta1, prosta2)? " << czy_proste_rownolegle(Prosta(w), Prosta(p,q)));
    Punkt nowy = punkt_przeciecia_prostych(Prosta(w), Prosta(p,q));
    LOG("Punkt_przeciecia_prostych(prosta1, prosta2) ======> (" << nowy.x << ", " << nowy.y << ")");

}
