from turtle import color, penup, pendown, dot, goto, pos



def pascal(n):
    L = []
    for i in range(n):
        L2 = [1]
        
        if i - 1 >= 0:
            t = L[i - 1]
            for j in range(len(t) - 1):
                L2.append(t[j] + t[j + 1])
            L2.append(1)

        
        L.append(L2)
    return L

print(pascal(5))





color = 'black'

def move(x, y):
    penup()
    goto(x, y)
    pendown()


def drawLine(L):
    base = pos()
    
    for x in L:
        if x % 2 != 0:
            dot(10)
            move(pos()[0] + 20, pos()[1])
        else:
            move(pos()[0] + 20, pos()[1])
    move(base[0], base[1])

def drawPascal(n):
    P = pascal(n)
    for e in P:
        drawLine(e)
        move(pos()[0] - 10, pos()[1] - 10)



drawPascal(20)








        
                
        
