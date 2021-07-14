S = set()
S2 = set()
S3 = set()

with open('slowa.txt', 'rb') as f:
    while True:
        line = f.readline()
        if line: 
            S.add(line)
        else:
            break


for e in S:
    e = str(e.decode()[:-1])
    S2.add(e)


for e in S2:
    er = e[::-1]
    if (er, e) not in S3:
        if er in S2:
            S3.add((e, er))

for e in S3:
    print(e)


