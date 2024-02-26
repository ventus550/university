
def AE(n):
    L = [x for x in range(2, n)]


    for i in range(len(L)):
        if L[i] != 0:
            for j in range(i + 1, len(L)):
                if L[j] % L[i] == 0:
                    L[j] = 0
                    
    return  [x for x in L if x != 0]
            
def isP(n):
    s = str(n)
    l = len(s)
    
    for i in range(l // 2):
        if s[i] != s[l - i - 1]:
            return False
    return True


        
def palindromy(a, b):
    prime_numbers = [x for x in AE(b) if x >= a and isP(x)]
        
    print(prime_numbers)


palindromy(10, 1000)
