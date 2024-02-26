from decimal import Decimal


def vat_faktura(lista, c = 0.23):
	return sum(lista) * c

def vat_paragon(lista, c = 0.23):
	return sum(c * x for x in lista)

zakupy = [0.2, 0.5, 4.59, 6]
print(vat_faktura(zakupy) == vat_paragon(zakupy))

zakupy_dec = [Decimal(x) for x in ["0.2", "0.5", "4.59", "6"]]
print(vat_faktura(zakupy_dec, Decimal("0.23")) == vat_paragon(zakupy_dec, Decimal("0.23")))