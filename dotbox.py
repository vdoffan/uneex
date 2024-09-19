import sys

min_x,max_x = sys.float_info.max, sys.float_info.min
min_y,max_y = sys.float_info.max, sys.float_info.min
min_z,max_z = sys.float_info.max, sys.float_info.min

while True:
    str = input()
    if str == "":
        break
    x, y, z = map(float, str.split(','))
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)
    min_z = min(min_z, z)
    max_z = max(max_z, z)

if min_x == sys.float_info.max:
    print(0)
else:
    ans = (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
    print(ans)
