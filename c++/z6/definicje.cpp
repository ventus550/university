#include <vector>
#include <cmath>
#include <sstream>

using namespace std;

string strp(const double d, const int n = 1) {
    ostringstream out;
    out.precision(n);
    out << fixed << d;
    return out.str();
}


class wyrazenie {
    public:
        virtual double oblicz() = 0;
        virtual string opis() = 0;
        int priorytet = 0;
};

class liczba : public wyrazenie {
    private:
        const double val;

    public:
        liczba(const double v) : val(v) {}
        double oblicz() {return val;}
        string opis() {return strp(val);}
};

class stala : public wyrazenie {
    protected:
        double val;
        string nazwa;

    public:
        virtual double oblicz() {return val;}
        string opis() {return nazwa;}
};

class pi : public stala {
    public:
        pi() {val = 3.14; nazwa = "pi";}
};

class e : public stala {
    public:
        e() {val = 2.71; nazwa = "e";}
};

class fi : public stala {
    public:
        fi() {val = 1.61; nazwa = "fi";}
};


class zmienna : public wyrazenie {
    private:
        static vector<pair<string, double>> v;
        string var;

    public:
        static void let(string var, double val) {
            for(int i = 0; i < v.size(); i++) {
                if(v[i].first == var) {
                    v[i].second = val;
                    return;
                }
            }
            v.push_back(make_pair(var, val));
        }

       static double extract(string var) {

            for(int i = 0; i < v.size(); i++) {
                if(v[i].first == var) {
                    return v[i].second;
                }
            }
            return -1;
       }

       zmienna(string var) {
            this->var = var;
            let(var, 0);
       }
       double oblicz() {return extract(var);}
       string opis() {return var;}
};
vector<pair<string, double>> zmienna::v;

class operator1arg : public wyrazenie {
    protected:
        wyrazenie *v;
        string nazwa;
        string nawias(string str) {return "(" + str + ")";}

    public:
        virtual double oblicz() {return 0;}
        string opis() {return nazwa;}
};

class sine : public operator1arg {
    public:
        sine(wyrazenie *v) {this->v = v; nazwa = "sin" + nawias(v->opis());}
        double oblicz() {
            return sin(v->oblicz());
        }
};

class cosine : public operator1arg {
    public:
        cosine(wyrazenie *v) {this->v = v; nazwa = "cos" + nawias(v->opis());}
        double oblicz() {
            return cos(v->oblicz());
        }
};

class expt : public operator1arg {
    public:
        expt(wyrazenie *v) {this->v = v; nazwa = "exp" + nawias(v->opis());}
        double oblicz() {
            return exp(v->oblicz());
        }
};

class ln : public operator1arg {
    public:
        ln(wyrazenie *v) {this->v = v; nazwa = "ln" + nawias(v->opis());}
        double oblicz() {
            return log(v->oblicz());
        }
};

class bezwzgl : public operator1arg {
    public:
        bezwzgl(wyrazenie *v) {this->v = v; nazwa = "bezwzgl" + nawias(v->opis());}
        double oblicz() {
            return abs(v->oblicz());
        }
};

class przeciw : public operator1arg {
    public:
        przeciw(wyrazenie *v) {this->v = v; nazwa = "przeciw" + nawias(v->opis());}
        double oblicz() {
            return -(v->oblicz());
        }
};

class odwrot : public operator1arg {
    public:
        odwrot(wyrazenie *v) {this->v = v; nazwa = "odwrot" + nawias(v->opis());}
        double oblicz() {
            return 1/(v->oblicz());
        }
};




class operator2arg : public operator1arg {
    protected:
        string left, right;
        wyrazenie *w1, *w2;
};

class dodaj : public operator2arg {
    public:
        dodaj(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 2;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            nazwa = left + " + " + right;
        }
        double oblicz() {
            return w1->oblicz() + w2->oblicz();
        }
};

class odejmij : public operator2arg {

    public:
        odejmij(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 2;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w2->priorytet == this->priorytet)
                right = nawias(right);

            nazwa = left + " - " + right;
        }

        double oblicz() {
            return w1->oblicz() - w2->oblicz();

        }
};

class mnoz : public operator2arg {
    public:
        mnoz(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 1;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w1->priorytet > this->priorytet) {
                left = nawias(left);
            }
            if(w2->priorytet > this->priorytet) {
                right = nawias(right);
            }

            nazwa = left + " * " + right;
        }
        double oblicz() {
            return w1->oblicz() * w2->oblicz();

        }
};

class dziel : public operator2arg {
    public:
        dziel(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 1;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w1->priorytet > this->priorytet) {
                left = nawias(left);
            }
            if(w2->priorytet > this->priorytet) {
                right = nawias(right);
            }

            nazwa = left + " / " + right;
        }

        double oblicz() {
            return w1->oblicz() / w2->oblicz();
        }
};

class modulo : public operator2arg {
    public:
        modulo(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 1;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w1->priorytet > this->priorytet) {
                left = nawias(left);
            }
            if(w2->priorytet > this->priorytet) {
                right = nawias(right);
            }

            nazwa = left + " % " + right;
        }
        double oblicz() {
            return int(w1->oblicz()) % int(w2->oblicz());
        }
};

class potega : public operator2arg {
    public:
        potega(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 1;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w1->priorytet > this->priorytet) {
                left = nawias(left);
            }
            if(w2->priorytet > this->priorytet) {
                right = nawias(right);
            }

            nazwa = left + "^" + right;
        }

        double oblicz() {
            return pow(w1->oblicz(), w2->oblicz());
        }
};

class logarytm : public operator2arg {
    public:
        logarytm(wyrazenie *w1, wyrazenie *w2) {
            priorytet = 1;
            left = w1->opis();
            right = w2->opis();
            this->w1 = w1;
            this->w2 = w2;

            if(w1->priorytet > this->priorytet) {
                left = nawias(left);
            }
            if(w2->priorytet > this->priorytet) {
                right = nawias(right);
            }

            nazwa = "log(" + left + "," + right + ")";
        }
        double oblicz() {
            return log(w1->oblicz()) / log(w2->oblicz());
        }
};

