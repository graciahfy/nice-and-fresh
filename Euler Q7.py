#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

c = 0
dict = []
while c < 10002:
    for num in range(2, 1000000):
        if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               c = c + 1
               dict.append(num)
