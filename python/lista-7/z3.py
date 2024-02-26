LALKA = {}

with open('lalka.txt', encoding = 'utf8') as f:
    for line in f:
        for word in line.split():
            w_s = word.strip(',.;"<>\|$%^&*()!?/_—')
            if w_s in LALKA:
                LALKA.update({w_s: LALKA[w_s] + 1})
            else:
                LALKA.update({w_s: 1})

                
def top10(a):
    L = sorted([(a, b) for a,b in LALKA.items()], key=lambda x: -len(x[0]) * (x[1]**a))
    for i in range(10):
        print(L[i])
    

top10(1)
