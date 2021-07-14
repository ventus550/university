def QS(L):
    print('rec')
    if len(L) == 1:
        return [L[0]]

    
    #sort
    
    b = 0
    e = len(L) - 1
    print(b, e)
    x = L[0]


    while(b < e):
        while(L[b] < x):
            b += 1
        while(L[e] > x):
            e -= 1
        
        print('b:',b,' e:',e)
        #if b < e:
        L[b], L[e] = L[e], L[b]
        b += 1
        e -= 1
            
    return QS(L[:b]) + QS(L[b:])
