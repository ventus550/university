
def usun_nawiasy(n):
    new = ''
    w_nawiasie = 0
    for i in range(len(n)):
        if n[i] == '(':
            w_nawiasie += 1

        if w_nawiasie == 0:
            new += n[i]

        if n[i] == ')':
            w_nawiasie -= 1
    
    return new

print(usun_nawiasy("Ala ma kota (perskiego(test(bbbbbb))aaa)"))
