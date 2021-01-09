# What is the largest prime factor of the number 600851475143 ?
a = 600851475143
for i in range(2, a):
    if a%i == 0:
        print i
