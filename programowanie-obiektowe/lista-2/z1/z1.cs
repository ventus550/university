using System;
using System.Collections.Generic;


namespace z1
{
    class IntStream
    {
        public int counter = 0;
        virtual public int next()
        { 
            if(eos() == false)
            {
                counter += 1;
                return counter;
            }
            reset();
            return 1;
        }
        public bool eos()
        {
            if (counter < 0)
            {
                return true;
            }
            return false;
        }
        virtual public void reset()
        {
            counter = 0;
        }
    }

    class PrimeStream : IntStream
    {
        List<int> prime_numbers = new List<int>();
        bool is_prime(int num)
        {
            if (counter == 0)
                counter = 2;

            foreach (int e in prime_numbers)
            {
                if (num % e == 0)
                    return false;
            }
            return true;
        }

        override public void reset()
        {
            counter = 2;
            prime_numbers = new List<int>();

        }

        override public int next()
        {

            while (is_prime(counter) == false)
            {

                if (counter == int.MaxValue)
                {
                    return counter;
                }

                counter += 1;

                if (eos())
                    reset();
            }
            prime_numbers.Add(counter);
            return counter;

        }
    }


    class RandomStream : IntStream
    {
        Random rand = new Random();
        override public int next()
        {
            return rand.Next(10);
        }
    }


    class RandomWordStream
    {
        RandomStream rs = new RandomStream();
        PrimeStream ps = new PrimeStream();
        public string next()
        {
            string str = "";
            int p = ps.next();
            for(int i = 0; i < p; i++)
            {
                str += rs.next().ToString();
            }
            return str;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {

            Console.WriteLine("\nRandom_Stream");
            RandomStream rs = new RandomStream();
            for (uint i = 0; i <= 10; i++)
                Console.WriteLine(rs.next());


            Console.WriteLine("\nPrime_Stream");
            PrimeStream ps = new PrimeStream();
            for (uint i = 0; i <= 10; i++)
                Console.WriteLine(ps.next());



            Console.WriteLine("\nRandom_Word_Stream");
            RandomWordStream rws = new RandomWordStream();
            for (uint i = 0; i <= 10; i++)
                Console.WriteLine(rws.next());

        }
    }
}







