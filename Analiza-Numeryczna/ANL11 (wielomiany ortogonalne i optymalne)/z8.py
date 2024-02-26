import matplotlib.pyplot as plt

fig, axs = plt.subplots(5,2, figsize=(15, 15))
plt.subplots_adjust(hspace=0.5)

X = []
with open("punkty.csv") as f:
    for line in f:
        line = [float(f) for f in line.strip().split(",")]
        X += [line]

X.sort(key=lambda x : x[0])
T = [x[0] for x in X]; Y = [x[1] for x in X]

# a) --------------------------
def f(t):
    return (t+3.6)*(t-2.1)*(t-3.7)

axs[0][0].set_title('f(t) i punkty X')
axs[0][0].plot(T, [f(t) for t in T])
axs[0][0].scatter(T, Y, c = "#ff7f0e")

# b) Lagrange --------------------------
def lmbd(k, x):
    res = 1
    for j in range(len(T)):
        if j == k:
            continue
        res *= (x-T[j])/(T[k]-T[j])
    return res

def L(x):
    res = 0
    for k in range(len(T)):
        res += Y[k]*lmbd(k, x)
    return res

xaxis = [x*0.02 for x in range(-250, 300)]
axs[0][1].set_title("Wielomian interpolacyjny Lagrange'a")
axs[0][1].scatter(T, Y, c = "#ff7f0e")
axs[0][1].plot(xaxis, [L(x) for x in xaxis])
axs[0][1].set_ylim(-10, 50)

'''# b) Newton --------------------------
def b(k):

    def prod(k, i):
        p = 1
        for j in range(0, k+1):
            if j == i:
                continue
            p *= T[i] - T[j]
        return p

    res = 0
    for i in range(0, k+1):
        res += Y[i]/prod(k, i)

    return res

def N(x):
    res = 0
    for k in range(len(T)):
        p = b(k)
        for i in range(k):
            p *= x-T[i]
        res += p
    return res

xaxis = [x*0.02 for x in range(-250, 300)]
axs[2].set_title('Wielomian interpolacyjny Newtona')
axs[2].scatter(T, Y, c = "#ff7f0e")
axs[2].plot(xaxis, [N(x) for x in xaxis])
axs[2].set_ylim(0, 50)'''


# c) ----------------------
class Memo:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]



def dot_product(f, g):
    res = 0
    for k in range(len(T)):
        res += f(T[k])*g(T[k])
    return res

@Memo
def a(k):
    return dot_product(f, P(k))/dot_product(P(k),P(k))
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
    if k == 1:
        return x - c(1)
    return (x - c(k)) * P(k-1)(x) - d(k) * P(k-2)(x)

def P(k):
    return lambda x: Pk(k, x)


def W(m):
    def calcW(x):
        res = 0
        for k in range(m):
            res += a(k)*P(k)(x)
        return res
    return calcW


for i in range(2, 9):
    axs[i//2][i%2].set_title("Optymalny wielomian interpolacyjny stopnia " + str(i))
    axs[i//2][i%2].scatter(T, Y, c = "#ff7f0e")
    axs[i//2][i%2].plot(xaxis, [W(i)(x) for x in xaxis])
    axs[i//2][i%2].set_ylim(-10, 50)
fig.delaxes(axs[4][1])
plt.show()










