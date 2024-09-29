
counts = [[0 for _ in range(101)] for _ in range(101)]

while True:
    line = input().strip()
    if not line:
        break

    parts = line.split(',')
    if len(parts) != 2:
        continue

    x = int(parts[0].strip())
    y = int(parts[1].strip())
    if 1 <= x <= 100 and 1 <= y <= 100:
        counts[x][y] += 1

for x in range(1, 101):
    for y in range(1, 101):
        for _ in range(counts[x][y]):
            print(f"{x}, {y}")

