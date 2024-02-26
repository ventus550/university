class ListItem:
    def __init__(self, e):
        self.e = e
        self.n = None

    def __str__(self):
        return str(self.e)


class LinkedList:
    def __init__(self, elems):
        self.first = None
        self.last = None
        self.length = 0

        for e in elems:
            self.append(e)

    def append(self, e):
        new = ListItem(e)
        if self.first == None:
            self.first = new
            self.last = new
        else:
            self.last.n = new
            self.last = new
        self.length += 1

    def __add__(self, other):
        self.append(other)
        return self

    def __iadd__(self, other):
        self.append(other)
        return self

    def __mul__(self, m):
        return LinkedList([e * m for e in list(self)])


    def __len__(self):
        return self.length

    def __iter__(self):
        elem = self.first
        while elem:
            yield elem.e
            elem = elem.n

    def iterator_li(self):
        elem = self.first
        while elem:
            yield elem
            elem = elem.n

    def __getitem__(self, i):
        pos = 0
        for e in self:
            if pos == i or pos == len(self) + i:
                return e
            pos += 1
        raise IndexError

    def __setitem__(self, i, a):
        pos = 0
        for li in self.iterator_li():
            if pos == i:
                li.e = a
                return
            pos += 1
        raise IndexError

    def __str__(self):
        elems = [str(e) for e in list(self)]
        # elems = map(str, list(elems))
        return '-[' + ', '.join(elems) + ']-'

    def __delitem__(self, i):
        if len(self) == 0:
            raise IndexError
        if i >= len(self):
            raise IndexError

        if len(self) == 1:
            self.first = None
            self.last = None
        elif i == 0:
            self.first = self.first.n
            self.length -= 1
        else:
            elem = self.first
            for _ in range(i - 1):
                elem = elem.n
            elem.n = elem.n.n
        self.length -= 1


L = LinkedList([2, 3, 4, 5, 5, 6, 7])
L2 = LinkedList([8, 5])

L[2] = 44


print(L * 2)

del L[5]
print(L)

print(L[-1])