def test(GL):
    for x in GL:
        print(x)


def push(L, GL):
    newL = []
    for i in range(len(L)):
        newL.append(set(L[i]))
    if newL not in GL:
        GL.append(newL)

def z5(GL):
    res = []

    def rec(main, sup):
        print(main, sup)

        if sup != []:
            push([main] + [sup], res)
        else:
            push([main],res)

        for i in range(1, len(main) - 1):
            #L = main[:i], [main[i]], main[i + 1:]

            A = main[:i]
            B = [main[i]]
            C = main[i + 1:]

            if sup != []:
                L = [A] + [B] + [C] + [sup]
            else:
                L = [A] + [B] + [C]
            push(L, res)


            rec(A, B+C+sup)
            rec(A + B, C+sup)





    rec(GL, [])
    test(res)



z5([1,2,3,4,5])

