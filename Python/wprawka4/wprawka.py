

upper = set()
lower = set()
special = []
numbers = []

def register(p):
    with open('users.db', encoding = 'utf-8') as f:
        for x in f:
            if ':' in x:
                line = x.split(sep = ':')
                if p == line[1].split()[0]:
                    raise Exception("Znajduje się w users.db")
        

    
    for x in p:
        if x.isupper():
            upper.add(x)
        elif x.islower():
            lower.add(x)
        elif x in '[@_!#$%^&*()<>?/\|}{~:]':
            special.append(x)
        elif x.isnumeric():
            numbers.append(x)

    if len(upper) < 2:
        raise Exception("Zawiera mniej niż 2 różne duże litery")
    if len(lower) < 2:
        raise Exception("Zawiera mniej niż 2 różne małe litery")
    if len(special) < 2:
        raise Exception("Zawiera mniej niż 2 znaki specjalne")
    if len(numbers) < 2:
        raise Exception("Zawiera mniej niż 2 cyfry")







p = input('Wprowadz haslo')

try:
    register(p)
except Exception as e:
    print(e)
else:
    print("Rejestracja przebiegla pomyslnie")
