
def a(L):
    S = set()

    
    def rec(ls):
        if len(ls) == 0:
            S.add(0)
            return
        
        S.add(sum(ls))
        for i in range(len(ls)):
            rec(ls[:i] + ls[i+1:])
    rec(L)

    print(sorted(list(S)))

#a([1,2,3,100])

def b(A, B, N, seq):
    if len(seq) == N:
        print(seq)
    if len(seq) > N:
        return
    for i in range(A, B):
        b(i, B, N, seq + [i])
            
b(2, 5, 18, [])
