from random import randint, choice



def place(ls, v):
    rand = randint(0, len(ls) - 1) 
    if ls[rand] == -1:
        ls[rand] = v
    else:
        place(ls, v)
        

def randperm(n):
    new = [-1 for i in range(n)]
    
    for x in range(n):
        place(new, x)

    
    return new


#x = randperm(10**6)
print(randperm(1000))
