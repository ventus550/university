def a(a, b):
    t = a
    while(t % b != 0):
        t = t + a
    return t


def b(a, b):
    x = a
    y = b
    
    if a < b:
        a = a + b
        b = a - b
        a = a - b

    while b > 0:
        a = a % b
        
        a = a + b
        b = a - b
        a = a - b

    x = x / a
    y = y / a

    return x, y
        
