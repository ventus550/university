using System;

namespace names2
{

    public class Item<T>
    {
        public T val;
        public Item<T> next;
        public Item<T> prev;
        public Item(T val)
        {
            this.val = val;
            next = null;
            prev = null;
        }
    }

    public class Lista<T> {
        Item<T> head, tail;
        public Lista() {
            head = null;
            tail = null;
        }
        public bool empty() {
            if (head == null && tail == null)
                return true;
            return false;
        }
        void add_when_empty(Item<T> item) {
            if(empty()) {
                head = item;
                tail = item;
            }
        }

        public void append(T val) {

            Item<T> new_item = new Item<T>(val);
            new_item.val = val;
            new_item.prev = tail;
            if(tail != null)
                tail.next = new_item;
            add_when_empty(new_item);
            tail = new_item;    
        }

        public void insert(T val) {
            
            Item<T> new_item = new Item<T>(val);
            new_item.val = val;
            new_item.next = head;
            if(head != null)
                head.prev = new_item;

            add_when_empty(new_item);
            head = new_item;     
        }

        public Item<T> pop() {
            if (empty())
                return null;
            
            Item<T> prev_head = head;
            head = head.next;
            prev_head.next = null;

            if(head == null)
                tail = null; 
            else
                head.prev = null;      
            
            return prev_head; 
        }

        public Item<T> remove() {
            if (empty())
                return null;

            Item<T> prev_tail = tail;
            tail = tail.prev;
            prev_tail.prev = null;

            if(tail == null)
                head = null;
            else
                tail.next = null;

            return prev_tail; 
        }

        public void print() {
            string str = "[";
            Item<T> p = head;
            if(p != null) {
                str += p.val;
                p = p.next;
            }
            while(p != null) {
                str += ", " + p.val;
                p = p.next;
            }
            Console.WriteLine(str + "]");
               
        }
    }
}
