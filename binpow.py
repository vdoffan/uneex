def BinPow(a, n, f):
    power = n - 1
    res = a
    while power > 0:
        if power % 2 == 1:
            res = f(res, a)
        a = f(a, a)
        power //= 2
    return res
