input_str = input().strip()

parts = input_str.split(',')

M = int(parts[0].strip())
N = int(parts[1].strip())

grid = [[0 for _ in range(M)] for _ in range(N)]

top = 0
bottom = N - 1
left = 0
right = M - 1

num = 0

while top <= bottom and left <= right:
    for col in range(left, right + 1):
        grid[top][col] = num % 10
        num += 1
    top += 1
    
    for row in range(top, bottom + 1):
        grid[row][right] = num % 10
        num += 1
    right -= 1
    
    if top <= bottom:
        for col in range(right, left - 1, -1):
            grid[bottom][col] = num % 10
            num += 1
        bottom -= 1
    
    if left <= right:
        for row in range(bottom, top - 1, -1):
            grid[row][left] = num % 10
            num += 1
        left += 1

for row in grid:
    print(' '.join(str(num) for num in row))