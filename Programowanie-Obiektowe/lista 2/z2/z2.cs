using System;

namespace z2
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

    class Array
    {
        Item head;
        Item last;  
        int size = 0;

        void insert(int val)
        {
            Item new_item = new Item(0);
            new_item.next = null;
            new_item.prev = head;
            new_item.idx = size;
            new_item.val = val;
            size += 1;

            if (head != null)
                head.next = new_item;
            else
                last = new_item;

            head = new_item;
        }

        Item findItem(int i)
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

        public int get(int i)
        {
            if(i >= size || i < 0)
                throw new System.ArgumentException("Index out of range", "original");

            Item found = findItem(i);

            return found.val;
        }

        
        public void set(int i, int val)
        {
            if(i < 0)
                throw new System.ArgumentException("Index out of range", "original");

            if(i < size)
            {
                Item found = findItem(i);
                found.val = val;
            } 
            else
            {
                while (size < i)
                    insert(0);
                insert(val);
            }
        }

        public void print()
        {
            Item item = findItem(0);
            string str = "[" + item.val.ToString();

            for(int i = 1; i < size; i++)
            {
                item = findItem(i);
                str += ", " + item.val.ToString();
            }

            str += "]";

            Console.WriteLine(str);

        }




        public Array(int s, int e)
        {
            for(int i = s; i < e; i++)
            {
                insert(0);
            }
        }



    }


    class Program
    {
        static void Main(string[] args)
        {

            Array a1 = new Array(0, 100);
            Array a2 = new Array(0, 100);
            Array a3 = new Array(0, 100);

            for (int i = 0; i < 100; i++)
            {
                a1.set(i, i);
                a2.set(i, i % 2);
            }

            for (int i = 0; i < 100; i++)
                a3.set(i, a1.get(i) + a2.get(i));

            a3.print();
        }
    }
}
