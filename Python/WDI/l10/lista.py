class ListItem:
    def __init__(self,value):
        self.val = value
        self.next = None

def lprint(ls, prt=True):
    L = []
    e = ls
    while e != None:
        L.append(e.val)
        e = e.next
    if prt:
        print(L)
    return L


#1. Wypisanie na standardowym wyjściu wszystkich dodatnich elementów z listy.
def findPositive(ls):
    while ls != None:
        if ls.val > 0:
            print(ls.val)
        ls = ls.next


#2. Dołączenie nowego elementu na koniec listy
def gorszy_pomysl(ls, nval):
    new = ListItem(nval)
    ls.next = new
    return ls


def add(ls, nval):
    while ls.next != None:
        ls = ls.next
    ls.next = ListItem(nval)


#------testing------
A = ListItem(0)
for x in range(1, 10):
    add(A, x)

B = ListItem(0)
for x in range(1, 10):
    add(B, (-(5%x))**(x % 2 + 1))
#-------\testing-----


#3. Usunięcie ostatniego elementu z listy.
def removeLast(ls):
    while ls.next.next != None:
        ls = ls.next
    ls.next = None

#4. Dołączenie jednej listy na koniec drugiej.
def cat(ls1, ls2):
    pointer = ls1.next
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = ls2

    return ls1



#5. Usunięcie z listy wszystkich elementów o podanej wartości pola val.
def removeVal(ls, rval):
    while ls.val == rval:
        ls = ls.next
        if ls == None:
            return ls


    base = ls
    while ls != None and ls.next != None:
        if ls.next.val == rval:
            ls.next = ls.next.next
        else:
            ls = ls.next

    return base

#6. Napisz funkcję wypisującą na standardowym wyjściu elementy listy w odwrotnej
#kolejności do ich występowania w liście. Nie należy przy tym zmieniać kolejności
#elementów w liście.

def rec(ls):
    if ls != None:
        rec(ls.next)
        print(ls.val)







#7. Napisz funkcję umożliwiającą odwrócenie kolejności elementów w liście.
def reverse(ls):
    prev = ls
    ls = ls.next
    prev.next = None

    while ls != None:
        t = ls
        ls = ls.next
        t.next = prev
        prev = t


    return prev


def reverse2(list):
    prev = None
    current = list
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    list = prev
    return list

#8. Napisz funkcję, która rozdzieli daną listę na dwie podlisty: jedną zawierającą elementy
#z kluczami dodatnimi a drugą – elementy z kluczami ujemnymi.

def lsplit(ls):
    base = ls
    isSorted = False

    while not isSorted:
        isSorted = True
        while ls.next != None:
            if ls.val > ls.next.val:
                isSorted = False
                ls.val, ls.next.val = ls.next.val, ls.val
            ls = ls.next
        ls = base

    ls1 = base
    while ls.next != None:
        if ls.next.val >= 0:
            ls2 = ls.next
            ls.next = None
            break
        ls = ls.next

    return ls2



#9.  Zaproponuj typ danych dla elementów listy dwukierunkowej, tj. takiej, w której każdy
#element zawiera wskaźnik na następny i wskaźnik na poprzedni element w liście
#(elementy pierwszy i ostatni mają odpowiednie wskaźniki ustawione na NULL/None).
#Napisz funkcje realizujące operacje kolejkowe na takiej liście: dodanie elementu na
#koniec kolejki, usunięcie elementu z początku kolejki

class LItem:
    parent = None

    def __init__(self,value):
        self.val = value
        self.next = None
        self.prev = None
        if LItem.parent == None:
            LItem.parent = self

    def add(self, nval):
        new = LItem(nval)
        LItem.parent.next = new
        new.prev = LItem.parent
        LItem.parent = new

    def pop(self):
        if self != None:
            return self.next
        else:
            return None
