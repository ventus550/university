import numpy as np

def tabliczka(x1, x2, y1, y2):
	X = np.arange(x1, x2+1, 1)
	Y = np.arange(y1, y2+1, 1).reshape(-1,1)
	R = Y * X

	R = np.hstack((Y, R))
	R = np.vstack( (np.array([0] + list(X)), R) )

	print(str(R).replace("]", " ").replace("[", " ").replace("0", " ", 1)) 

tabliczka(3, 5, 2, 4)
tabliczka(0, 10, 0, 12)

