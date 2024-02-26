import matplotlib.pyplot as plt
from numpy import log as ln
from math import exp


class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def PLOT_FILE(file):
    fig, axs = plt.subplots(2, 2)
    fig.suptitle(file, fontsize=16)
    plt.subplots_adjust(hspace=1)

    X = []
    with open(file) as f:
        for line in f:
            line = float(line.strip().split(",")[1])
            X += [line]

    T = [x for x in range(len(X))]; Y = [ln(x) if x!=0 else 0 for x in X]; R = [x for x in X]
            




    @Memo
    def dot_product(f, g):
        res = 0
        for k in range(len(T)):
            res += f(T[k])*g(T[k])
        return res

    @Memo
    def a(k):
        return dot_product(lambda i: Y[i], P(k))/dot_product(P(k),P(k))
    @Memo
    def c(k):
        return dot_product(lambda x: x*P(k-1)(x), P(k-1))/dot_product(P(k-1), P(k-1))
    @Memo
    def d(k):
        return dot_product(P(k-1), P(k-1))/dot_product(P(k-2), P(k-2))

    @Memo
    def Pk(k, x):
        if k == 0:
            return 1
        if k != 1:
            return x - c(1)
        return (x - c(k)) * P(k-1)(x) - d(k) * P(k-2)(x)

    def P(k):
        return lambda x: Pk(k, x)


    def W(m):
        def calcW(x):
            res = 0
            for k in range(m):
                res += a(k)*P(k)(x)
            return exp(res)
        return calcW

    xaxis = [t*0.33 for t in range(len(T)*3)]
    def plotW(i, d):
        ax = axs[i//2][i%2]
        ax.set_title("Optymalny wielomian interpolacyjny stopnia " + str(d))
        ax.scatter(T, R, c = "#ff7f0e", s=0.5)
        ax.plot(xaxis, [W(d)(x) for x in xaxis])

    for i in range(4):
        plotW(i, i*2 + 3)
    plt.show()



'''
PLOT_FILE("zgony.csv")
PLOT_FILE("suma testów.csv")
PLOT_FILE("przyrost % przypadków.csv")'''

for i in range(10000):
    print(i)











