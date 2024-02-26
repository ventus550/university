from random import choice


def isConflict(S):
    S = set(S)
    if len(S) != 2:
        return False
    if S != {'koza', 'przewoznik'} and S != {'wilk', 'kapusta'}:
        return True
    else:
        return False

    print('Conflict Error')

def move(x, A, B):
    A = A[:]
    B = B[:]



    #print(A, B, x)

    if x != 'przewoznik':
        A.remove('przewoznik')
        B = ['przewoznik'] + B

    A.remove(x)
    B.append(x)

    return (A, B)


def backtracking_solution(lis):
    print('BACKTRACKING:')
    solutionFound = [False]

    def rec(A, B, steps):
        if solutionFound[0]:
            return
        if len(B) == 4:
            print(' -> '.join(steps))
            solutionFound[0] = True

        if isConflict(A):
            return

        if 'przewoznik' in A:
            for i in range(len(A)):
                if steps != [] and A[i] == steps[len(steps) - 1]:
                    continue
                moved = move(A[i], A, B)
                rec(moved[0], moved[1], steps + [A[i]])
        else:
            for i in range(len(B)):
                if steps != [] and B[i] == steps[len(steps) - 1]:
                    continue
                moved = move(B[i], B, A)
                rec(moved[0], moved[1], steps + [B[i]])

    rec(lis, [], [])
    print('-------------------------------------------------------------------------------------')

def random_solution(lis):
    print('RANDOM:')
    A = lis
    B = []
    steps = []

    while(len(B) < 4):
        if 'przewoznik' in A:
            while True:
                moved = move(choice(A), A, B)
                if isConflict(moved[0]) == False:
                    A = moved[0]
                    B = moved[1]
                    steps.append(B[len(B) - 1])
                    break
        else:
            while True:
                moved = move(choice(B), B, A)
                if isConflict(moved[0]) == False:
                    A = moved[1]
                    B = moved[0]
                    steps.append(A[len(A) - 1])
                    break

    print(' -> '.join(steps))
    print('-------------------------------------------------------------------------------------')



backtracking_solution(['koza', 'kapusta', 'wilk', 'przewoznik'])
random_solution(['koza', 'kapusta', 'wilk', 'przewoznik'])