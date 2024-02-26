def test(GL):
    for x in GL:
        print(x)
    print('COUNT:', len(GL))

#czasem wrzucam list(list(list)) = 'unhashable type: list'
def push(L, GL):
    print('PUSH:', L)
    newL = []
    for i in range(len(L)):
        newL.append(set(L[i]))
    if newL not in GL:
        GL.append(newL)

def z5(GL):
    res = []

    def rec(main, sup):
        if True: #len(main) == 1:
            push([main] + sup, res)
            #return main
        for i in range(len(main) - 1):
            A = main[:i+1]
            B = main[i+1:]
            #print(A,B, sup + B)
            #push(rec(A, sup), GL)
            t = sup[:]
            t.append(B)
            print([B] + sup, t)
            rec(A, [B] + sup)



        return main
    rec(GL, [])
    test(res)



z5([1,2,3,4])
#dla 4 wyników ma być 15
