from itertools import count, accumulate
from operator import add


def pierwiastek(n):
    """Zadanie 2 lista 2 -- obliczanie podłogi z pierwiastka z n

        Przykłady:
        >>> pierwiastek(100)
        10

        >>> pierwiastek(3)
        1

        >>> pierwiastek(-1)
        0
        """

    for k, val in enumerate(accumulate((2*i - 1 for i in count(1)), add)):
        if val > n:
            return k
