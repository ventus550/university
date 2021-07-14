for x in open('A.MATRIX'):
    A = eval(x)
for x in open('B.MATRIX'):
    B = eval(x)

if len(A[0]) != len(B):
    raise Exception("Error")



M = []
for i in range(len(A)): #dla każdego wiersza w A:
    L = []
    for j in range(len(B[0])): #dla każdej kolumny w B:
        suma = 0
        for k in range(len(B)): #dla każdego wyrazu:
            suma += A[i][k]*B[k][j]
            
        L.append(suma)
    M.append(L)

print(M)






