from math import exp, pi
# Defining Function


#k=6
'''def f(x):
	if x == 0:
		return 0.000000000001
	denominator = 48
	numerator = x**2 * exp(-x/2)
	r = numerator/denominator
	return r

def g(x):
	if x == 0:
		return 0.000000000001
	return (exp(-x/2)*x*(x - 4)) / 96
'''

#k=1
'''def f(x):
	if x == 0:
		return 0.000000000001

	return (2*pi)**0.5 * x**(-0.5) * exp(-0.5*x)


def g(x):
	if x == 0:
		return 0.000000000001
	
	return (2*pi)**0.5 * exp(-x/2) * (x**(-0.5) + 0.5*x**0.5) / -2
'''

'''
def f(x):
    return x**3 - 5*x - 9

def g(x):
    return 3*x**2 - 5'''

# Implementing Newton Raphson Method

def newtonRaphson(x0,e,N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        
        x1 = x0 - f(x0)/g(x0)
        print('Iteration-%d, x1 = %0.6f and f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        
        if step > N:
            flag = 0
            break
        
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Input Section
x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

# Converting x0 and e to float
x0 = float(x0)
e = float(e)

# Converting N to integer
N = int(N)


#Note: You can combine above three section like this
# x0 = float(input('Enter Guess: '))
# e = float(input('Tolerable Error: '))
# N = int(input('Maximum Step: '))

# Starting Newton Raphson Method
newtonRaphson(x0,e,N)