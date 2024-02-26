from time import time

t0 = time()
n = 6
s = (n * (n**2 + 1)) / 2
board = [[0 for _ in range(n)] for _ in range(n)]
numbers = [1 for i in range(n**2 + 1)]

def checkRow(y):
    res = 0
    for i in range(n):
        res += board[y][i]
        
    if res == s:
        
        return True
    return False

def checkColumn(x):
    res = 0
    for i in range(n):
        res += board[i][x]

    if res == s:
        return True
    
    return False

def checkDiagonals():
    res1 = 0
    res2 = 0
    for i in range(n):
        res1 += board[i][i]
        res2 += board[n - i - 1][i]
    if res1 != s or res2 != s:
        return False
    
    return True

def putNumber(depth, rec, x, y):
    for i in range(1, n**2 + 1):
        if numbers[i] == 1:
            numbers[i] = 0
            if board[y][x] != 0:
                numbers[board[y][x]] = 1

            board[y][x] = i

                
            if depth == 0:
                if checkDiagonals():
                    print(board)
                    t1 = time()
                    print(t1-t0)
                    
                    
            elif rec < depth:
                putNumber(depth, rec+1, x, y+1)
                
            elif rec == depth:
                if checkColumn(x):
                    putNumber(depth, rec+1, x+1, y)
                
                
            elif rec < 2 * depth:
                putNumber(depth, rec+1, x+1, y)
                
            elif rec == 2 * depth:
                if checkRow(y):
                    putNumber(depth - 1, 0, n - depth, 0)
                    
            numbers[i] = 1
            board[y][x] = 0
                

putNumber(n - 1, 0, 0, 0)


                
