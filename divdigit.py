def divdigit(n):
    str_n = str(n)
    cnt = 0
    for i in str_n:
        if i == '0':
            continue
        if n % int(i) == 0:
            cnt += 1
    return cnt
