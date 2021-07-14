



def kon(s):
    board = [[0 for _ in range(s)] for _ in range(s)]
    board[2][2] = 1

    def rec(pos, B, seq):
        for c in [(-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1)]:
            x = pos[0] + c[0]
            y = pos[1] + c[1]
            try:
                if x*y >= 0 and x+y >= 0 and B[x][y] == 0:
                    B[x][y] = 1
                    seq.append(c)
                    
                    if len(seq) == s*s:
                        print('seq:', seq)
                    
                    rec((x,y), B, seq)
            except:
                {}

    rec((2,2), board, [(0,0)])

kon(5)
                    
