def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

points = []
while True:
    s = input()
    if s == '':
        break
    x_str, y_str = s.strip().split(',')
    x = int(x_str)
    y = int(y_str)
    points.append((x, y))

n = len(points)

if n <= 2:
    print("True")
    exit()

points = sorted(set(points))

lower = []
for p in points:
    while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
        lower.pop()
    lower.append(p)

upper = []
for p in reversed(points):
    while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
        upper.pop()
    upper.append(p)

convex_hull = lower[:-1] + upper[:-1]
convex_hull = set(convex_hull)

if len(convex_hull) == n:
    print("True")
else:
    print("False")
