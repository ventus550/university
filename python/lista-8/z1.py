from random import choice

POL_ANG = {}
BROWN = {}

with open('pol_ang.txt', encoding = 'utf-8') as f:
    for line in f:
        line = line[:-1]
        if '=' not in line:
            continue

        words = line.split(sep = '=')
        if len(words) != 2:
            continue
        if words[0] not in POL_ANG:
            POL_ANG.update({words[0]: [words[1]]})
        else:
            POL_ANG[words[0]].append(words[1])


with open('brown.txt', encoding = 'utf-8') as f:
    for line in f:
        line = line.strip('\n,.;"\'!@#$%^&*()?')

        words = line.split()
        for i in range(len(words)):    
            if words[i] not in BROWN:
                BROWN.update({words[i]: 1})
            else:
                BROWN[words[i]] += 1

def translate(sentence):
    tx = ''
    for word in sentence.split():
        print(word)
        if word not in POL_ANG:
            tx += ' [?]'
            continue

        T = POL_ANG[word]
        mx = 0
        for i in range(len(T)):
            if T[i] not in BROWN:
                T[i] = (T[i], 0)
            else:
                if mx < BROWN[T[i]]: mx = BROWN[T[i]]
                T[i] = (T[i], BROWN[T[i]])
        
        T = [x[0] for x in T if x[1] == mx]
        tx += " " + str(choice(T))

    return tx


sentence = "iść do miasto dla zakupy"
print(translate(sentence))






















