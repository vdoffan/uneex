from math import sqrt

def nonprime(n = 0):
    cur = n + 1
    if cur == 1: yield cur
    while True:
        for i in range(2, int(sqrt(cur) + 1)):
            if cur % i == 0:
                yield cur
                break
        cur += 1
