from decimal import Decimal, getcontext

A = Decimal(input())
E = int(input())

extra = 5
getcontext().prec = E + extra

def arctan(x):
    x = Decimal(x)
    result = x
    term = x
    n = 1
    while True:
        term *= -x * x
        denom = 2 * n + 1
        delta = term / denom
        result += delta
        if delta.copy_abs() < Decimal('1e-{}'.format(E + extra - 1)):
            break
        n += 1
    return result

def compute_pi():
    pi = Decimal(16) * arctan(Decimal(1)/5) - Decimal(4) * arctan(Decimal(1)/239)
    return pi

def sin(x):
    x = Decimal(x)
    result = x
    term = x
    n = 1
    while True:
        term *= -x * x / ((2 * n) * (2 * n + 1))
        result += term
        if term.copy_abs() < Decimal('1e-{}'.format(E + extra - 1)):
            break
        n += 1
    return result

def cos(x):
    x = Decimal(x)
    result = Decimal(1)
    term = Decimal(1)
    n = 1
    while True:
        term *= -x * x / ((2 * n - 1) * (2 * n))
        result += term
        if term.copy_abs() < Decimal('1e-{}'.format(E + extra - 1)):
            break
        n += 1
    return result

pi = compute_pi()

theta = A * (pi / Decimal(200))

sin_theta = sin(theta)
cos_theta = cos(theta)

tan_theta = sin_theta / cos_theta

getcontext().prec = E

tan = str(tan_theta.normalize())

if tan.find('.') == -1:
    tan += '.' + '0'*(E-1)
    print(tan)
else:
    print(tan_theta.normalize())
