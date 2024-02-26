#include <iostream>
#include <map>
#include <vector>
#include <typeinfo>
#include <cmath>

//debug mode
#if 0
    #define LOG(x) clog << x << endl;
#else
    #define LOG(x);
#endif

using namespace std;
namespace kalkulator {

    class symbol {
        public:
            string value;
            virtual bool match(string str) = 0;
            virtual double calculate(vector<symbol*> &v) = 0;

    };

    class funkcja : public symbol {
        public:
            double read(vector<symbol*> &v) {
                if(v.size() == 0) {
                    cerr << "STACK IS EMPTY" << endl;
                    return -1;
                }

                symbol *s = v.back();
                v.pop_back();
                LOG("Popped: " << s->value);
                return s->calculate(v);
            }

            funkcja(string val) {
                this->value = val;
            }
    };

    class dodawanie : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return read(v) + read(v);
            }

            bool match(string str) {
                return str == "+";
            }

            dodawanie(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class odejmowanie : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return -(read(v) - read(v));
            }

            bool match(string str) {
                return str == "-";
            }

            odejmowanie(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class mnozenie : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return read(v) * read(v);
            }

            bool match(string str) {
                return str == "*";
            }

            mnozenie(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class dzielenie : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return (1 / read(v)) * read(v);
            }

            bool match(string str) {
                return str == "/";
            }

            dzielenie(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class modulo : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                double t = read(v);
                return (int)read(v) % (int)t;
            }

            bool match(string str) {
                return str == "%";
            }

            modulo(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class min_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return min(read(v), read(v));
            }

            bool match(string str) {
                return str == "min";
            }

            min_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class max_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return max(read(v), read(v));
            }

            bool match(string str) {
                return str == "max";
            }

            max_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class log_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                //double t = read(v);
                return logl(read(v)) / logl(read(v));
            }

            bool match(string str) {
                return str == "log";
            }

            log_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class pow_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                double t = read(v);
                return pow(read(v), t);
            }

            bool match(string str) {
                return str == "pow";
            }

            pow_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class abs_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                double t = read(v);
                if(t > 0)
                    return t;
                return -t;
            }

            bool match(string str) {
                return str == "abs";
            }

            abs_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class sgn : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                double t = read(v);
                if(t >= 0)
                    return 1;
                return -1;
            }

            bool match(string str) {
                return str == "sgn";
            }

            sgn(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class floor_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return floor(read(v));
            }

            bool match(string str) {
                return str == "floor";
            }

            floor_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class ceil_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return ceil(read(v));
            }

            bool match(string str) {
                return str == "ceil";
            }

            ceil_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class frac : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                double p;
                return modf(read(v), &p);
            }

            bool match(string str) {
                return str == "frac";
            }

            frac(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class sin_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return sin(read(v));
            }

            bool match(string str) {
                return str == "sin";
            }

            sin_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class cos_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return cos(read(v));
            }

            bool match(string str) {
                return str == "cos";
            }

            cos_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class atan_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return atan(read(v));
            }

            bool match(string str) {
                return str == "atan";
            }

            atan_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class acot_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return atan(1/read(v));
            }

            bool match(string str) {
                return str == "acot";
            }

            acot_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class ln_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return logl(read(v)) / logl(2.718281828459);
            }

            bool match(string str) {
                return str == "ln";
            }

            ln_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class exp_ : public funkcja {
        public:
            double calculate(vector<symbol*> &v) {
                return exp(read(v));
            }

            bool match(string str) {
                return str == "exp";
            }

            exp_(string val) : funkcja(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };



    class operand : public symbol {
        public:
            operand(string val) {
                this->value = val;
            }
    };

    class liczba : public operand {
        public:
            double calculate(vector<symbol*> &v) {
                return stod(this->value);
            }
            bool match(string str) {
                if(!(str[0] == '-' || isdigit(str[0])))
                    return 0;

                str.erase(0, 1);

                for(char c : str)
                    if(!isdigit(c) && c != '.')
                        return 0;
                return 1;
            }

            liczba(string val) : operand(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };

    class zmienna : public operand {
        public:
            static map<string, double> assoc;
            double calculate(vector<symbol*> &v) {
                if(assoc.find(this->value) != assoc.end()){
                    return assoc[this->value];
                }
                clog << "Unknown identifier " << this->value << endl;
                return -1.0;
            }

            bool match(string str) {
                return str.length() <= 7 &&
                       str != "print" &&
                       str != "assign" &&
                       str != "clear" &&
                       str != "exit";
            };
            zmienna(string val) : operand(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };
    map<string, double> zmienna::assoc;

    class stala : public operand {
        map<string, double> assoc = {
            {"pi", 3.141592653589},
            {"fi", 1.618033988750},
            {"e", 2.718281828459}};

        public:
            double calculate(vector<symbol*> &v) {
                return assoc[this->value];
            }

            bool match(string str) {
                return assoc.find(str) != assoc.end();
            }

            stala(string val) : operand(val) {
                if(!match(val)) {
                    throw invalid_argument("Failed to match");
                }
            };
    };
}

using namespace kalkulator;
class Stack {

    vector<symbol*> v;

    template<class C>
    bool match(string str) {
        try {
            v.push_back(new C(str));
            LOG(" Successfully matched with " << typeid(C).name());
            return 1;

        }
        catch(invalid_argument) {
            LOG(" Failed to match with "  << typeid(C).name());
            return 0;
        }
    }

    public:
        Stack() {};

        bool parse(string str) {
            LOG("Matching " << str << "...");
            return  match<odejmowanie>(str) ||
                    match<liczba>(str)      ||
                    match<stala>(str)       ||
                    match<dodawanie>(str)   ||
                    match<mnozenie>(str)    ||
                    match<dzielenie>(str)   ||
                    match<modulo>(str)      ||
                    match<min_>(str)        ||
                    match<max_>(str)        ||
                    match<log_>(str)        ||
                    match<pow_>(str)        ||
                    match<abs_>(str)        ||
                    match<sgn>(str)         ||
                    match<floor_>(str)      ||
                    match<ceil_>(str)       ||
                    match<frac>(str)        ||
                    match<sin_>(str)        ||
                    match<cos_>(str)        ||
                    match<atan_>(str)       ||
                    match<acot_>(str)       ||
                    match<ln_>(str)         ||
                    match<exp_>(str)        ||
                    match<zmienna>(str);
        }

        void add(string str) {
            if(!parse(str))
                cerr << "NO MATCH FOR " << str << endl;
        }

        double pullc() {
            if(v.size() == 0) {
                cerr << "STACK IS EMPTY" << endl;
                return 0;
            }

            symbol *s = v.back();
            v.pop_back();
            LOG("Popped: " << s->value);
            return s->calculate(v);
        }

        void user_input() {
            string line;
            getline(cin, line);
            vector<string> words;

            size_t pos = line.find(' ');
            size_t pos_begin = 0;
            while( pos != string::npos ) {
                words.push_back( line.substr( pos_begin, pos - pos_begin ) );
                pos_begin = pos + 1;
                pos = line.find( ' ', pos_begin );
            }
            words.push_back( line.substr( pos_begin, std::min( pos, line.size() ) - pos_begin + 1 ));

            string cmd = words[0];

            if(cmd == "assign") {
                string var = words.back();

                for(int i = 1; i < words.size() - 2; i++)
                    add(words[i]);
                zmienna::assoc[var] = pullc();

            } else {

                if(cmd == "print") {
                    for(int i = 1; i < words.size(); i++)
                        add(words[i]);
                    cout << pullc() << endl;
                    return;
                }

                if(cmd == "clear") {
                    zmienna::assoc.clear();
                    return;
                }

                if(cmd == "exit") {
                    exit(1);
                    return;
                }

                cerr << "Command unrecognized" << endl;
            }

        }
};

int main()
{

    Stack *S = new Stack();
    while(true)
        S->user_input();
    free(S);
    return 0;
}
