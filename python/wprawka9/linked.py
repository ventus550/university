
class ListItem:
    def __init__(self, value):
        self.val = value
        self.nxt = None

def mkLL(L):
    newList = ListItem(L[0])
    base = newList
    for x in L[1:]:
        newList.nxt = ListItem(x)
        newList = newList.nxt

    return base

L = mkLL([1,2,3,4])
print('List to LL:   -----------------------------------')
print(L.val, L.nxt.val, L.nxt.nxt.val, L.nxt.nxt.nxt.val)


def printLL(ll):
    x = ll

    while x != None:
        print(x.val)
        x = x.nxt

print('print:   -----------------------------------')
printLL(L)


def printReversedLL(ll):
    if ll.nxt != None:
        printReversedLL(ll.nxt)
    print(ll.val)

print('reversed:   -----------------------------------')
printReversedLL(L)

def reverseLL(ll):
    p = ll
    this = ll.nxt
    p.nxt = None

    while this != None:
        t = this.nxt
        this.nxt = p
        p = this
        this = t

    return p


#testy
print('----------')
printReversedLL(mkLL([1, 2, 3, 5]))
print('----------')
printLL(reverseLL(mkLL([1, 2, 3, 5])))
print('----------')