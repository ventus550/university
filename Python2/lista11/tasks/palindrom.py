def palindrom(text):
    '''Zadanie 2 lista 1 -- sprawdzanie czy zdanie jest palindromem'''

    banned = "!\",.;: `'"
    text = "".join([ch for ch in text.lower().strip() if ch not in banned])

    for i in range(len(text) // 2):
        if text[i] != text[-i-1]:
            return False
    return True


if __name__ == '__main__':
    palindrom('a'*10**7)
