class runners {

    static class Biegacz extends Thread
    {
        private int tick = 1;
        private int num;
        public Biegacz(int num) { this.num = num; }
        public void run() {
            while (this.tick < 400000) {
                this.tick++;
                if ((this.tick % 50000) == 0)
                    System.out.println("Thread #" + num);
            }
    }

    }


    public static void main(String args[]) {

        Biegacz [] runners = new Biegacz[2];
        for (int i = 0; i < 2; i++)
        {
            runners[i] = new Biegacz(i);
        }

        for (int i = 0; i < 2; i++)
            runners[i].start();
    }
}