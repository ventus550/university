

'''
---- poor concept --------
class ListItem:
    def __init__(self,value):
        self.pointTo = self
        self.val = value
        self.next = None
    def add(self, nval):
        new = ListItem(nval)
        self.pointTo.next = new
        self.pointTo = new
'''

class ListItem:
    pointer = None

    def __init__(self,value):
        self.val = value
        self.next = None
        if ListItem.pointer == None:
            ListItem.pointer = self
    def add(self, nval):
        new = ListItem(nval)
        ListItem.pointer.next = new
        ListItem.pointer = new
x = ListItem(0)
x.add(1)
x.add(-5)

print(x.val, x.next.val, x.next.next.val)



'''
class test():
    print('new class')
    cval = 'new?'

    def __init__(self):
        print('init')

t = test() #print 'new class', 'init'
t2 = test() #print 'init'

print(t.cval) #print 'new?'
test.cval = 10
print(t.cval) #print '10'

t.dodaned = 'nowy atrybut'
print(t.dodaned)
'''