from itertools import product

class Formula:
	@staticmethod
	def tautologia(formula):
		if not isinstance(formula, Formula):
			raise LogicError("accepting formulas only")	
		sformula = formula.simplify()
		symbols = formula.symbols()
		bools = [True, False]
		return all( sformula.oblicz(dict(zip(symbols, c)))
		for c in map(lambda x: (x[0], x[1][0], x[1][1]), product(bools, product(bools, bools))) )
		
	def __add__(self, other):
		return And(self, other)

	def __mul__(self, other):
		return Or(self, other)



class Zmienna(Formula):
	def __init__(self, symbol : str):
		super().__init__()
		if symbol.isnumeric():
			raise LogicError("passing numeric symbols is not permitted")
		self.symbol = symbol
	
	def __str__(self):
		return self.symbol
	
	def oblicz(self, zmienne : dict):
		if self.symbol in zmienne:
			return zmienne[self.symbol]
		raise UndefinedError()
	
	def simplify(self):
		return Zmienna(self.symbol)
	
	def symbols(self):
		return {self.symbol}



class Stala(Formula):
	def __init__(self, value : bool):
		super().__init__()
		if not isinstance(value, bool) :
			raise LogicError("passing values other than boolean is not permitted")
		self.value = value

	def __str__(self):
		return str(self.value)
	
	def oblicz(self, zmienne : dict):
		return self.value

	def simplify(self):
		return Stala(self.value)
	
	def symbols(self):
		return set()



class Not(Formula):
	def __init__(self, formula : Formula):
		super().__init__()
		self.formula = formula
	
	def __str__(self):
		return f'¬{str(self.formula)}'
	
	def oblicz(self, zmienne : dict):
		return not self.formula.oblicz(zmienne)
	
	def simplify(self):
		if isinstance(self.formula, Stala):
			return Stala(not self.formula.value)
		return self
	
	def symbols(self):
		return self.formula.symbols()


class And(Formula):
	def __init__(self, first : Formula, second : Formula):
		super().__init__()
		self.first = first
		self.second = second
	
	def __str__(self):
		return f'({str(self.first)} ⋀ {str(self.second)})'
	
	def oblicz(self, zmienne : dict):
		return self.first.oblicz(zmienne) and self.second.oblicz(zmienne)

	def simplify(self):
		sfirst = self.first.simplify()
		ssecond = self.second.simplify()

		if isinstance(sfirst, Stala) and isinstance(ssecond, Stala) and sfirst.value and ssecond.value:
			return Stala(True)

		if (isinstance(sfirst, Stala) and not sfirst.value
		or (isinstance(ssecond, Stala) and not ssecond.value)):
			return Stala(False)

		if isinstance(sfirst, Stala) and sfirst.value:
			return ssecond
		if isinstance(ssecond, Stala) and ssecond.value:
			return sfirst
		
		return And(sfirst, ssecond)
	
	def symbols(self):
		return self.first.symbols() | self.second.symbols() 



class Or(Formula):
	def __init__(self, first : Formula, second : Formula):
		super().__init__()
		self.first = first
		self.second = second
	
	def __str__(self):
		return f'({str(self.first)} ⋁ {str(self.second)})'
	
	def oblicz(self, zmienne : dict):
		return self.first.oblicz(zmienne) or self.second.oblicz(zmienne)
	
	def simplify(self):
		sfirst = self.first.simplify()
		ssecond = self.second.simplify()

		if isinstance(sfirst, Stala) and isinstance(ssecond, Stala) and not sfirst.value and not ssecond.value:
			return Stala(False)

		if (isinstance(sfirst, Stala) and sfirst.value
		or (isinstance(ssecond, Stala) and ssecond.value)):
			return Stala(True)

		if isinstance(sfirst, Stala) and not sfirst.value:
			return ssecond
		if isinstance(ssecond, Stala) and not ssecond.value:
			return sfirst
		return Or(sfirst, ssecond)
	
	def symbols(self):
		return self.first.symbols() | self.second.symbols() 



class LogicError(Exception):
	'''Raise when Formula encounters an error'''

class UndefinedError(LogicError):
	'''Raise when variable is missing a value'''



fi = Or(Not(Zmienna("x")), And(Zmienna("y"), Stala(True)))
print(fi)
print(fi + fi)
print(fi * fi)


true = Stala(True)
false = Stala(False)
pi = Or(false, Or(And(fi, false), Zmienna("p")))
print(pi, ">>>", pi.simplify())

print( Formula.tautologia(fi) )
print( Formula.tautologia( Or(pi, Not(pi)) ) )
