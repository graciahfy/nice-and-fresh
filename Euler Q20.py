#Find the sum of the digits in the number 100!
a = 100
l = [a]
b = a
for i in range(2, a + 1):
    a = a - 1
    b = a * b
c = str(b)
res = [int(x) for x in str(c)]
d = sum(res)
print(d)
