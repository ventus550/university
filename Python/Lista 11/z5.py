import matplotlib.pyplot as plt


def wybory(a):
    def M_list(M, N, a):
        M = int(M)
        divs = []
        res = [0 for x in N]
        for i in range(len(N)):
            for j in range(1, M+1):
                if N[i] == '–':
                    break
                divs.append( (float(N[i]) / j**a, i) )
        divs.sort(key=lambda x: x[0], reverse=True)


        for i in range(M):
            res[divs[i][1]] += 1

        for i in range(len(N)):
            if N[i] == '–':
                continue
            res[i] = (float(N[i])/100)*M - res[i]

        return res


    with open('wyniki_wyborow.tsv', encoding='utf-8') as f:
        et = f.readline().split()
        komitety = et[3:-1]

        SUM = [0 for x in komitety]
        for x in f:
            Ms = x.split()[2]
            stats = x.split()[3:-1]

            SUM = [x + y for x, y in zip(SUM, M_list(Ms, stats, a))]
        return SUM




values = [[] for i in range(6)]
args = [i/10 for i in range(1, 20)]

for i in range(1, 20):
    res = wybory(i/10)

    for j in range(len(res)):
        values[j].append(res[j])

for i in range(6):
    plt.plot(args, values[i], label=i)

plt.show()