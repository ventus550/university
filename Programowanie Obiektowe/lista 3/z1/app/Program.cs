using System;
using names2;

namespace names1
{
    class Program
    {
        static void Main(string[] args)
        {
            Lista<int> L = new Lista<int>();
            L.insert(10);
            L.print();  

            L.append(12);
            L.print();

            Console.WriteLine(L.pop());
            L.print();

            L.remove();
            L.print();

            Console.WriteLine(L.remove());

            L.insert(5);
            L.print();
        }
    }
}
