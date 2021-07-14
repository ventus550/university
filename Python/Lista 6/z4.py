
def split2(txt):
    L = []
    t_str = ''
    for i in range(len(txt)):
        if txt[i].isspace():
            if t_str > '':
                L.append(t_str)
                t_str = ''
        else:
            t_str += txt[i]
    return L

print(split2("   Ala   ma kota "))
