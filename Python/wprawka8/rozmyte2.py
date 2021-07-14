import matplotlib.pyplot as plt
def calcProximity(x, P):
    L = []
    for p in P:
        L.append(1/(1+(x-p)**2))
    return max(L)

def mplot(s):
    L = sorted(list(s))
    A = [x[0] for x in L]
    B = [x[1] for x in L]

    plt.plot(A, B, "o")
    plt.show()

class BlurredSet:
    X = {0,1,2,3,4,5,6,7,8,9}

    def __init__(self, proximity, s):
        self.contents = set()
        noDups = set()
        for e in s:
            noDups.add(e)
        for e in noDups:
            p = calcProximity(e, proximity)
            if p > 0:
                self.contents.add((e, p))

    def __contains__(self, item):
        for x in self.contents:
            if x == item:
                return True
        return False

    def __eq__(self, other):
        for x in self.contents:
            if x not in other.contents:
                return False

        return True

    def __mul__(self, other):
        new = set()
        for x in self.contents:
            for y in other.contents:
                if x[0] == y[0]:
                    new.add( (x[0], min(x[1], y[1])) )
        return new
    def __add__(self, other):
        t  = set()
        new = set()
        for x in self.contents:
            t.add(x[0])
        for x in other.contents:
            t.add(x[0])

        for x in t:
            a = 0
            b = 0
            for y in self.contents:
                if y[0] == x:
                    a = y[1]
                    break
            for y in other.contents:
                if y[0] == x:
                    b = y[1]
                    break
            new.add( (x, max(a, b)) )
        return new

    def dopelnienie(self):
        new = set()
        for x in BlurredSet.X:
            isIN = False
            for y in self.contents:
                if x == y[0]:
                    new.add( (x, 1 - y[1]))
                    isIN = True
            if isIN == False:
                new.add( (x, 1))
        return new
    def mplot(self):
        L = sorted(list(self.contents))
        A = [x[0] for x in L]
        B = [x[1] for x in L]

        plt.plot(A, B, "o")
        plt.show()



    def __str__(self):
        return '{' + ', '.join([str(x) for x in self.contents]) + '}'
        


t1 = BlurredSet([7], [5, 6, 7, 8, 9])
print(t1)


t2 = BlurredSet([6], [4, 5, 6, 7, 8, 9])
print(t2)

print(t1 == t2)
print(t1 * t2)
print(t1 + t2)
print(t1.dopelnienie())
print(t1.mplot())
print(t2.mplot())
mplot(t1 + t2)
mplot(t1 * t2)
mplot(t1.dopelnienie())