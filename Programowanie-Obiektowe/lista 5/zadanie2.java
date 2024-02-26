import java.util.HashMap;

 class zadanie2 {

    interface Expression {
        public int oblicz(HashMap<Character, Integer> hs);
        public String toString();
    }

    static class Wyrażenie implements Expression {
        Expression e;

        Wyrażenie(Object obj) {
            if (obj instanceof Integer)
                this.e = new Const((int) obj);
            if (obj instanceof Character)
                this.e = new Variable((char) obj);
            if (obj instanceof Wyrażenie)
                this.e = ((Wyrażenie)obj).e;
        }
        

        public void add(Object n) {
            this.e = new AFormula('+', this.e, (new Wyrażenie(n)).e);
        }

        public void sub(Object n) {
            this.e = new AFormula('-', this.e, (new Wyrażenie(n)).e);
        }

        public void div(Object n) {
            this.e = new AFormula('/', this.e, (new Wyrażenie(n)).e);
        }

        public void mult(Object n) {
            this.e = new AFormula('*', this.e, new Wyrażenie(n).e);
        }

        public int oblicz(HashMap<Character, Integer> hs) {
            return e.oblicz(hs);
        }

        public String toString() {
            return e.toString();
        }

        public void print() {
            System.out.println(toString());
        }
    }


    static class AFormula implements Expression {
        char op;
        Expression left, right;

        int arithmetics(int a, int b) {
            switch(this.op) {
                case '+':
                    return a + b;
                case '-':
                    return a - b;
                case '*':
                    return a * b;
                case '/':
                    return a / b;
                default:
                    return -1;
            }
        }

        AFormula(char op, Expression left, Expression right) {
            this.op = op;
            this.left = left;
            this.right = right;
        }

        public int oblicz(HashMap<Character, Integer> hs) {
            return arithmetics(left.oblicz(hs), right.oblicz(hs));
        }

        public String toString() {
            return "(" + left.toString() + " " + String.valueOf(op) + " " + right.toString() + ")";
        }

    }

    static class Const implements Expression {
        int val;
        public Const(int val) {
            this.val = val;
        }

        public int oblicz(HashMap<Character, Integer> hs) {
            return this.val;
        }

        public String toString() {
            return String.valueOf(this.val);
        }
    }

    static class Variable implements Expression {
        char var;
        public Variable(char var) {
            this.var = var;
        }

        public int oblicz(HashMap<Character, Integer> hs) {
            return hs.get(this.var);
        }

        public String toString() {
            return String.valueOf(this.var);
        }
    }



    public static void main(String[] args) {
        Wyrażenie W = new Wyrażenie(1);
        Wyrażenie Q = new Wyrażenie(9);
        HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
        hm.put('x', 0);
        hm.put('y', 5);

        W.add(10);
        W.print();
        W.sub(3);
        W.print();
        System.out.println(W.oblicz(hm));

        W.mult('x');
        W.print();

        System.out.println(W.oblicz(hm));

        W.add('y');
        System.out.println(W.oblicz(hm));

        W.add(Q);
        W.print();

        Q.add(99);
        Q.add(999);

        W.add(Q);
        W.print();



    }
    

}