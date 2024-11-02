import math

def ispower(n):
    if n <= 1:
        print("NO")
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if math.log(n, i) == math.ceil(math.log(n, i)) and math.log(n, i) > 1:
            print("YES")
            return
    print("NO")
    return

n = int(input())
ispower(n)