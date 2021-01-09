# A palindromic number reads the same both ways. Find the largest palindrome made from the product of two 3-digit numbers.
for num in range(810000, 998002):
    newpa = str(num)
    repa = newpa[::-1]
    if newpa == repa:
        for i in range(900, 999):
            if (num % i) == 0:
                b = num / i
                if b < 1000:
                    print(num, i)
