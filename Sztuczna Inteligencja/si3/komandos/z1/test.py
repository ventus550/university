from random import choice

component_functions = [lambda x: x**2, lambda y: y, lambda z: z + 1]

F = lambda x: x

for i in range(3):
	f = choice(component_functions)

	F = lambda x, F=F, f=f: F(f(x))

print(F(1))


#-----------------------------------



