maxlen, sublen = 1, 1
prev = int(input())
if prev == 0:
    print(0)
else:
    while True:
        cur = int(input())
        if cur == 0:
            break
        if (cur >= prev):
            sublen += 1
        else:
            maxlen = max(maxlen, sublen)
            sublen = 1
        prev = cur
    maxlen = max(maxlen, sublen)
    print(maxlen)
