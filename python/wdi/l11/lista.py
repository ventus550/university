class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

T = TreeItem(5)
def addBST(t, x):
    if x <= t.val:
        print('left(',t.val,')>', sep='', end='')
        if t.left != None:
            addBST(t.left, x)
        else:
            print('appended')
            t.left = TreeItem(x)
    else:
        print('right(',t.val,')>', sep='', end='')
        if t.right != None:
            addBST(t.right, x)
        else:
            print('appended')
            t.right = TreeItem(x)

for i in range(10):
    addBST(T, i%4)
print('---------------------------------------------------------')

# 2. Napisz funkcję, która dla parametru t wskazującego na korzeń drzewa binarnego
# zwraca jako wartość liczbę elementów w drzewie o korzeniu t.
def count_rec(t):
    if t == None:
        return 0
    print(t.val)
    return count_rec(t.left) + count_rec(t.right) + 1

# 3. Napisz funkcję, która dla parametru t zwraca jako wartość wysokość drzewa o korzeniu t.
def max_rec(t, h):
    if t == None:
        return h

    L = max_rec(t.left, h+1)
    R = max_rec(t.right, h+1)

    if R > L:
        return R
    else:
        return L

# 4. Napisz funkcję, która dla parametru t opisującego drzewo BST wypisuje
#(w porządku niemalejącym) wszystkie elementy dodatnie znajdujące się w drzewie
#o korzeniu t
def wypisz(t):
    if t != None:
        wypisz(t.left)
        if t.val > 0:
            print(t.val)
        wypisz(t.right)
wypisz(T)

# 5.  Napisz funkcję, która dla danego drzewa binarnego sprawdza czy jest ono drzewem BST
def isBST(t):
    L = t.left
    R = t.right

    if L == None and R == None:
        return True

    elif L != None and R != None:
        if L.val <= t.val and R.val > t.val:
            return isBST(L) and isBST(R)
        else:
            return False
    elif L != None and R == None:
        if L.val <= t.val:
            return isBST(L)
        else:
            return False
    elif L == None and R != None:
        if R.val > t.val:
            return isBST(R)
        else:
            return False


# 6. Napisz funkcję, która łączy dwa drzewa BST w jedno drzewo przy założeniu, że
# wszystkie wartości w pierwszym drzewie są mniejsze od najmniejszej wartości w drugim
# drzewie. Czas działania Twojej funkcji powinien być O(h), gdzie h to wysokość
# pierwszego drzewa.
def merge(t1, t2):
    while t1.left != None:
        t1 = t1.left
    t1.left = t2



# 8.Rotacją nazywamy operację przebudowy drzewa BST tak, aby wskazany węzeł u i
# jego wskazane dziecko v „zmieniły miejsca” w taki sposób, że u stanie się dzieckiem v.
# Podaj sposób na wykonanie rotacji w sytuacji, gdy v jest lewym dzieckiem u.
def rotate(u):
    v = u.left
    r = u.right

    u.left = v.left
    v.left = u

    u.right = v.right
    v.right = r

    return v












