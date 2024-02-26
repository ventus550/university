#include <iostream>

using namespace std;

template <typename T>
class List {
    class node {
        public:

            T val;
            node *next;

            node() {};
            node(T val, node *nxt) {this->val = val; this->next = nxt;};
            node(const node &n) {
                this->val = n.val;
                this->next = n.next;
            }
            node(node &&n) : val(move(n.val)) {
                n.val = NULL;
            }
            node &operator= (const T &t) {
                this->val = t;
                return *this;
            }
            node &operator= (const node &n) {
                this->val = n.val;
                return *this;
            }
            node &operator= (node &&n) {
                this->val = move(n.val);
                n.val = NULL;
                return *this;
            }
    };




    public:
        node* Head = NULL;

        List() {Head = NULL;}
        List(initializer_list<T> il){
            int length = il.size();
            for (auto it = std::rbegin(il); it != std::rend(il); ++it) {
                Head = new node(*it, Head);
            }
        }


        int len() {
            int k = 0;
            node *p = Head;

            while (p != NULL) {
                k++;
                p = p->next;
            }
            return k;
        }

        node &operator[] (int i) {
            if(i >= len()) {
                throw out_of_range("Index out of range");
            }
            node *p = Head;
            for(int k = 0; k < i; k++) {
                p = p->next;
            }
            return *p;
        }

        void insert(int i, T val) {
            if(i >= len()) {
                throw out_of_range("Index out of range");
            }
            node *p = Head;
            for(int k = 0; k < i; k++) {
                p = p->next;
            }
            p->val = val;
        }

        int find(T val) {
            node *p = Head;
            int k = 0;
            while(p != NULL) {
                if(p->val == val) {
                    return k;
                }
                p = p->next;
                k++;
            }
            return -1;
        }

        int remove(T val) {
            node *prev = Head;
            node *p = prev->next;
            while(p != NULL) {
                if(p->val == val) {
                    prev->next = p->next;
                    free(p);
                } else {
                    prev = prev->next;
                }
                p = p->next;
            }
            if (Head->val == val)
                Head = Head->next;
        }

        friend ostream &operator<< (ostream &out, List<T> &ls) {
            node *p = ls.Head;
            out << "[ ";
            while (p != NULL) {
                out << p->val;
                out << " ";
                p = p->next;
            }
            out << "]";
        }
};

template<typename T>
class less_or_equal {
    public:
        bool compare(T t1, T t2){
            return t1 <= t2;
        }
};

template<typename T>
class greater_or_equal {
    public:
        bool compare(T t1, T t2){
            return t1 >= t2;
        }
};

template<typename T = int, class operation = less_or_equal<T>>
bool check(List<T> &ls) {
    operation op;
    for(int i = 0; i < ls.len() - 1; i++) {
        if(op.compare(ls[i].val, ls[i+1].val) == false)
            return false;
    }
    return true;
}


template<typename T = int, class operation = less_or_equal<T>>
void sort(List<T> &ls)
{
    int i, j;
    operation op;
    for (i = 0; i < ls.len() - 1; i++)
        for (j = 0; j < ls.len()-i-1; j++)
            if (op.compare(ls[j].val, ls[j+1].val) == false) {
                T temp = ls[j].val;
                ls[j] = ls[j+1].val;
                ls[j+1] = temp;
            }
}






