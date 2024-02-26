

def F(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3*n + 1





def analiza_collatza(a, b):
    E = []
    for x in range(a, b):

        num = x
        energia = 0
        
        while(num > 1):
            energia += 1
            num = F(num)
        E.append(energia)
    
    #avg
    print('avg:', sum(E)/len(E))
    
    #max/min
    print('max/min:', max(E), min(E))
    
    #median
    E = sorted(E)
    l = len(E)
    print('median:', end= ' ')
    if l % 2 == 1:
        print(E[l // 2])
    else:
        print((E[l // 2] + E[l // 2 - 1]) / 2) 
        




analiza_collatza(2,8)

