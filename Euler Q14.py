#Longest Collatz sequence
lg = [0]
def Collatz():
    n = a
    sq = [n]
    while n != 1:
        if n%2 == 0:
            n = n/2
            sq.append(n)
        else:
            n = 3*n + 1
            sq.append(n)
    k = len(sq)
    if max(lg) < k:
        lg.append(k)
        print(a)




a = 1
while a < 1000000:
    Collatz()
    a = a + 1
