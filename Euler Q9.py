#There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

from sympy import *
a = Symbol('a')
b = Symbol('b')
k = solve([a ** 2 + b ** 2 - (1000 - a - b) ** 2], [a, b])
print(k)
