
def B(i,j):
    return 'B_%d_%d' % (i,j)

def maplist(f, L):
    return list(map(f, L))

def print_constraints(Cs, indent, d):
    position = indent
    #print (indent * ' ', end='')
    for c in Cs:
        writeln (c + ',')
        #print (c + ',', end=' ')
        position += len(c)
        if position > d:
            position = indent
            writeln ('')
            #print ()
            #print (indent * ' ', end='')

def C(L):
    return " ".join(L)

def get_rectangle(i, j):
    return (C([  B(i,j), "#= 1", "#==>", B(i-1,j), "+", B(i+1,j), "#>", "0"  ])+", "+
            C([  B(i,j), "#= 1", "#==>", B(i,j-1), "+", B(i,j+1), "#>", "0"  ]))

def get_diagonal(i, j):
    return (C([  B(i,j), "+", B(i+1, j+1), "#= 2", "#==>", B(i,j+1), "+", B(i+1, j), "#= 2"  ])+", "+
            C([  B(i,j), "+", B(i-1, j+1), "#= 2", "#==>", B(i,j+1), "+", B(i-1, j), "#= 2"  ]))

def domains(Vs):
    return [ q + ' in 0..1' for q in Vs ]

def storms(rows, cols, triples):
    writeln(':- use_module(library(clpfd)).')
    print("ROWS", rows)
    
    R = len(rows)
    C = len(cols)
    
    bs = [ B(i,j) for i in range(R) for j in range(C)]
    
    writeln('solve([' + ', '.join(bs) + ']) :- ')

    def get_column(j):
        return [B(i,j) for i in range(C)] 
            
    def get_raw(i):
        return [B(i,j) for j in range(R)]

    def rectangles():
        return [ get_rectangle(i,j) for i in range(R) for j in range(C) ]
    def diagonals():
        return [ get_diagonal(i,j) for i in range(R) for j in range(C) ]
    
    def COLS():
        return [ 'sum([' + ', '.join(get_column(c)) + '], #=, '  + str(cols[c]) + ')' for c in range(C) ]
    def ROWS():
        return [ 'sum([' + ', '.join(get_raw(r)) + '], #=, '  + str(rows[r]) + ')' for r in range(R) ]

    cs = domains(bs) + ROWS() + COLS() + rectangles() + diagonals()

    for i,j,val in triples:
        cs.append( '%s #= %d' % (B(i,j), val) )
    
    
    #TODO: add some constraints
    
    # writeln('    [%s] = [1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0],' % (', '.join(bs),)) #only for test 1

    print_constraints(cs, 4, 70)
    writeln('    labeling([ff], [' +  ', '.join(bs) + ']).' )
    writeln('')
    writeln(":- tell('prolog_result.txt'), solve(X), write(X), nl, told.")

def writeln(s):
    output.write(s + '\n')

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')

rows = maplist(int, txt[0].split())
cols = maplist(int, txt[1].split())
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(maplist(int, txt[i].split()))

storms(rows, cols, triples)            

#python3 validator.py zad5 python3 storms_for_students.py

