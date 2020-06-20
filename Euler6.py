# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

l = [i for i in range(101)]
a = sum(l)
print(a)
b = a**2
print(b)
t = []
for i in l: 
	c = i**2
	t.append(c)
	print(c)
d = sum(t)
print(d)

print(b - d)
	
