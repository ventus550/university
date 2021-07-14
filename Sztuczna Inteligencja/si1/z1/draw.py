from turtle import *
from time import sleep

def dist(p1, p2):
	return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def DRAW(seq):
	def draw_state(S):
		setworldcoordinates(0,0,10,10)
		hideturtle()

		def sq(x, y, c):
			penup()
			goto(x+1, y+1)
			pendown()
			
			fillcolor(c)
			begin_fill()
			for _ in range(4):
				forward(1)
				right(90)
			end_fill()
			penup()


		bk = S["blackK"]
		wk = S["whiteK"]
		wt = S["whiteT"]
		for i in range(8):
			for j in range(8):
				
				if i == bk[0] and j == bk[1]:
					sq(i, j, "blue")
				elif i == wk[0] and j == wk[1]:
					sq(i, j, "#800000")
				elif i == wt[0] and j == wt[1]:
					sq(i, j, "red")
				elif i == wt[0] or j == wt[1]:
					sq(i, j, "grey")
				elif dist((i,j), wk) < 2:
					sq(i, j, "grey")	
				else:
					sq(i, j, "white")
	
	tracer(0, 0)
	for state in seq:
		draw_state(state)
		sleep(1)
	done()