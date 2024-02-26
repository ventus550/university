import random
import sys
from copy import deepcopy
from collections import defaultdict as dd
from turtle import *

#####################################################
# turtle graphic
#####################################################
# tracer(0,1)

BOK = 50
SX = -100
SY = 0
M = 8


def kwadrat(x, y, kolor):
  fillcolor(kolor)
  pu()
  goto(SX + x * BOK, SY + y * BOK)
  pd()
  begin_fill()
  for i in range(4):
    fd(BOK)
    rt(90)
  end_fill() 

def kolko(x, y, kolor):
  fillcolor(kolor)

  pu()
  goto(SX + x * BOK + BOK/2, SY + y * BOK - BOK)
  pd()
  begin_fill()
  circle(BOK/2)
  end_fill() 

#####################################################

def initial_board():
    B = [ [None] * M for i in range(M)]
    B[3][3] = 1
    B[4][4] = 1
    B[3][4] = 0
    B[4][3] = 0
    return B

    
class Board:
    dirs  = [ (0,1), (1,0), (-1,0), (0,-1), (1,1), (-1,-1), (1,-1), (-1,1) ]
    
    
    def __init__(self, board = initial_board(), player = 0):
        self.board = []
        self.fields = set()
        self.player = player
        self.res = 0
        for i in range(M):
            I = []
            for j in range(M):
                bf = board[i][j]
                I.append(bf)
                if bf == None:   
                    self.fields.add( (j,i) )
                else:
                    self.res += bf*2 - 1
            self.board.append(I)
            
    
    def copy(self):
        return Board(self.board, self.player)
                             
    def __str__(self):
        s = ""
        for i in range(M):
            res = []
            for j in range(M):
                b = self.board[i][j]
                if b == None:
                    res.append('.')
                elif b == 1:
                    res.append('#')
                else:
                    res.append('o')
            s += "".join(res) + "\n"
        return s
        
    
    def show(self):
        for i in range(M):
            for j in range(M):
                kwadrat(j, i, 'green')
                
        for i in range(M):
            for j in range(M):                
                if self.board[i][j] == 1:
                    kolko(j, i, 'black')
                if self.board[i][j] == 0:
                    kolko(j, i, 'white')
                                   
    def moves(self):
        res = []
        for (x,y) in self.fields:
            if any( self.can_beat(x,y, direction) for direction in Board.dirs):
                res.append( (x,y) )
        return res               
    
    def can_beat(self, x,y, d):
        dx,dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x,y) == 1-self.player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x,y) == self.player
    
    def get(self, x,y):
        if 0 <= x < M and 0 <=y < M:
            return self.board[y][x]
        return None
                        
    def do_move(self, move):        
        if move == None:
            return
        x,y = move
        x0,y0 = move
        self.board[y][x] = self.player
        self.fields -= set([move])
        for dx,dy in self.dirs:
            x,y = x0,y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x,y) == 1-self.player:
              to_beat.append( (x,y) )
              x += dx
              y += dy
            if self.get(x,y) == self.player:              
                for (nx,ny) in to_beat:
                    self.board[ny][nx] = self.player
        self.player = 1-self.player
        return self
                                                     
    def result(self):
        return self.res
                
    def terminal(self):
        return not self.moves()

    def random_move(self):
        ms = self.moves()
        if ms:
            return random.choice(ms)
        return []    
    

'''self.player = 0
B = Board()

while True:
    B.draw()
    B.show()
    m = B.random_move(self.player)
    B.do_move(m, self.player)
    self.player = 1-self.player
    input()
    if B.terminal():
        break
    
B.draw()
B.show()
print ('Result', B.result())
input('Game over!')
  
       
sys.exit(0)     '''            
