def czyp(n):
    b = ''
    size = 0
    while n > 0:
        b = b + str(n % 2)
        n = n // 2
        size = size + 1


    
    for i in range(size // 2):
        if b[i] != b[size - 1 - i]:
            return False
    return True
