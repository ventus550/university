

def z5(SET):
    res = []

    def rec(main, sup):


        t = [main]
        if sup != set():
            t.append(sup)
        if t[::-1] not in res and t not in res:
            res.append(t)

        t = [main]
        for e in sup:
            t.append({e})
        if t[::-1] not in res and t not in res:
            res.append(t)



        for e in main:
            try:
                mc = main.copy()
                mc.discard(e)
                sc = sup.copy()
                sc.add(e)
                if len(sup) < len(main):
                    rec(mc, sc)
            except:
                {}

    rec(SET, set())


    print(res)


z5({1,2,3})