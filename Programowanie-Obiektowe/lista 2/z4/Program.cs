using System;
using System.Collections.Generic;

namespace z4
{
    class Item
    {
        public int val;
        public int idx;
        public Item next;
        public Item prev;
        public Item(int val)
        {
            this.val = val;
            next = null;
            prev = null;
        }
    }

    class ListaLeniwa
    {
        Random rnd = new Random();
        protected Item head;
        protected Item last;
        protected int SIZE = 0;


        protected void insert(int val)
        {
            Item new_item = new Item(0);
            new_item.next = null;
            new_item.prev = head;
            new_item.idx = SIZE;
            new_item.val = val;
            SIZE += 1;

            if (head != null)
                head.next = new_item;
            else
                last = new_item;

            head = new_item;
        }

        protected Item findItem(int i)
        {
            while (last.idx != i)
            {
                if (last.idx < i)
                    last = last.next;
                else
                    last = last.prev;
            }

            return last;
        }

        public int size()
        {
            return SIZE;
        }


        virtual public int element(int i)
        {
            if (i < 0)
                throw new System.ArgumentException("Index out of range", "original");

            while (i > SIZE)
                insert(rnd.Next());
            insert(rnd.Next());

            return findItem(i).val;
        }
        public void print()
        {
            if (SIZE == 0)
                Console.WriteLine("[]");
            else
            {
                Item item = findItem(0);
                string str = "[" + item.val.ToString();

                for (int i = 1; i < SIZE; i++)
                {
                    item = findItem(i);
                    str += ", " + item.val.ToString();
                }

                str += "]";

                Console.WriteLine(str);
            }
            

        }
    }

    class Pierwsze:ListaLeniwa
    {
        List<int> prime_numbers = new List<int>();
        int counter = 2;

        bool is_prime(int num)
        {
            foreach (int e in prime_numbers)
            {
                if (num % e == 0)
                    return false;
            }
            return true;
        }
        int generate_prime()
        {
            while (is_prime(counter) == false)
            {
                if (counter == int.MaxValue)
                {
                    return counter;
                }
                counter += 1;
            }
            prime_numbers.Add(counter);
            return counter;

        }


        override public int element(int i)
        {
            if (i < 0)
                throw new System.ArgumentException("Index out of range", "original");

            while (i > SIZE)
                insert(generate_prime());
            insert(generate_prime());

            return findItem(i).val;
        }

    }

    class Program
    {
        static void Main(string[] args)
        {
            ListaLeniwa LL = new ListaLeniwa();
            Console.WriteLine(LL.element(10));
            LL.print();
            Console.WriteLine(LL.element(10));


            Pierwsze p = new Pierwsze();
            Console.WriteLine(p.element(10));
            p.print();
            Console.WriteLine(p.element(0));




        }
    }
}
