import math

def biquad_solution(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return -1
            else:
                return 0
        else:
            if -c/b >= 0:
                root = math.sqrt(-c/b)
                return sorted([-root, root])
            else:
                return 0

    dis = b**2 - 4*a*c
    if dis < 0:
        return 0

    ans = []
    x1 = (-b + math.sqrt(dis)) / (2*a)
    x2 = (-b - math.sqrt(dis)) / (2*a)
    
    if x1 == 0 or x2 == 0:
        ans.append(0)
    if x1 > 0:
        root1 = math.sqrt(x1)
        ans.extend([-root1, root1])
    if x2 > 0:
        root2 = math.sqrt(x2)
        ans.extend([-root2, root2])

    if ans != []:
        return sorted(set(ans))
    else:
        return 0


a, b, c = map(float, input().split(','))
ans = biquad_solution(a, b, c)
if ans == 0 or ans == -1:
    print(ans)
else:
    print(' '.join(map(str, ans)))
