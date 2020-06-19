# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


h = input('Gimme a number: ')
k = int(h)
n = k - 1
t = k % n
l = []
while n > 1: 
	t = k%n 
	if t == 0: 
		l.append(n)
	n = n - 1
	
print("All the factors: ", l)

print("The largest factor: ", l[0])
