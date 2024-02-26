a = [0, 1, 2, 3, 5, 6, 7]

x = 8
lewy, prawy = 0, len(a)-1
while(lewy < prawy):
    k = (lewy + prawy) // 2
    if a[k] < x:
        lewy = k + 1
    else:
        prawy = k

print(lewy)
