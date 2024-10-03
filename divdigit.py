def divdigit(n):
    cnt = 0
    for digit in str(n):
        if digit != '0' and n % int(digit) == 0:
            cnt += 1
    return cnt