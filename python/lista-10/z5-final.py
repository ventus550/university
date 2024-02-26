

def z5(ls):
    res = []

    def connect(main, sup, mem, index):
        main = main.copy()
        mem = mem[:]

        main.add(mem[index])
        mem.remove(mem[index])
        rec(main, sup, mem)

    def create(main, sup, mem, index):
        main = main.copy()
        mem = mem[:]
        sup = sup[:]

        sup.append(main)
        main = {mem[index]}
        mem.remove(mem[index])
        rec(main, sup, mem)

    def rec(main, sup, mem):
        #raczej okey
        if len(mem) == 0:
            if sup + [main] not in res:
                res.append(sup + [main])
        else:
            for i in range(len(mem)):
                connect(main,sup,mem,i)
            create(main, sup, mem, 0)


    rec({ls[0]}, [], ls[1:])


    for x in res:
        print(x)
    print('Total:', len(res))


z5([1,2,3,4])