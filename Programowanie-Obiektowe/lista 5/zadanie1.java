
class Zadanie1 {

    interface Rank extends Comparable<Rank> {
        int getRank();
        String getName();
    }

    static class Soldier implements Rank {
        int rank;
        String name;

        public int getRank() {
            return this.rank;
        }

        public String getName() {
            return this.name;
        }

        public int compareTo(Rank rnk) {
            return Integer.signum(this.getRank() - rnk.getRank());
        }

        Soldier(int rank, String name) {
            this.rank = rank;
            this.name = name;
        }
    }

    static class Captain extends Soldier {
        Captain() {
            super(1, "Captain");
        }
    }

    static class Major extends Soldier {
        Major() {
            super(2, "Major");
        }
    }

    static class Colonel extends Soldier {
        Colonel() {
            super(3, "Colonel");
        }
    }

    static class General extends Soldier {
        General() {
            super(4, "General");
        }
    }


    static class SortedList implements Rank {
        static class Item {
            Rank itemRank;
            Item prev;

            Item(Rank itemRank, Item prev) {
                this.itemRank = itemRank;
                this.prev = prev;
            }
        }

        private Item tail;

        SortedList(Rank frst) {
            this.tail = new Item(frst, null);
        }

        SortedList() {}

        public String getName() {
            return "Group";
        }
        public int getRank() {
            if(tail == null)
                return 0;
            return this.tail.itemRank.getRank();
        }

        public int compareTo(Rank sl) {
            return Integer.signum(this.getRank() - sl.getRank());
        }

        public void add(Rank rnk) {

            if(this.tail == null) {
                tail = new Item(rnk, null);
                return;
            }

            if(tail.itemRank.compareTo(rnk) <= 0) {
                tail = new Item(rnk, tail);
            } else {
                Item p = tail;

                while(p.prev != null) {
                    if(p.prev.itemRank.compareTo(rnk) <= 0) {
                        Item insert = new Item(rnk, p.prev);
                        p.prev = insert;
                        return;
                    }
                    p = p.prev;
                }
                p.prev = new Item(rnk, null);
            }
        }


        public Rank pop() {
            Item p = tail;

            if(p == null) {
                return new SortedList();
            }

            if(p.prev == null) {
                Item t = tail;
                tail = null;
                return t.itemRank;
            }

            while(p.prev.prev != null) {
                p = p.prev;
            }

            Item t = p.prev;
            p.prev = null;
            return t.itemRank;
        }
        
        public void print() {
            String str = "";
            
            Item p = tail;
            while(p != null) {
                str = p.itemRank.getName() + "<" + p.itemRank.getRank() + "> " + str;
                p = p.prev;
            }
            System.out.println("[ " + str + "]");
            System.out.println("");
        }
        
    }


    public static void main(String[] args) {
        SortedList Batalion = new SortedList(new Colonel());
        Batalion.add(new General());
        Batalion.add(new Captain());
        Batalion.print();

        Batalion.add(new SortedList(new Captain()));
        Batalion.print();

        while(Batalion.getRank() != 0) {
            Batalion.pop();
            Batalion.print();
        }
    }
}