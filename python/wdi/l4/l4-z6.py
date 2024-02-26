def zapis(n):
    s = str(n)
    k = 0
    for i in range(10):
        is_in = False
        for x in s:
            if x == str(i):
                is_in = True
        if is_in:
            k = k + 1
    return k
