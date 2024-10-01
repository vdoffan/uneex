matrix = []
try:
    while True:
        line = input()
        if line == '':
            break
        row = [x.strip() for x in line.strip().split(',')]
        matrix.append(row)
except EOFError:
    pass

N = len(matrix)

size = 2 * N - 1
grid = [[None for _ in range(size)] for _ in range(size)]

for i in range(N):
    for j in range(N):
        r = i + j
        c = N - 1 + j - i
        grid[r][c] = matrix[i][j]

for c in range(size):
    elements = []
    for r in range(size):
        if grid[r][c] is not None:
            elements.append(grid[r][c])
            grid[r][c] = None

    r = size - 1
    for elem in reversed(elements):
        grid[r][c] = elem
        r -= 1

for row_idx in range(N - 1, size):
    output_row = []
    for c in range(size):
        if grid[row_idx][c] is not None:
            output_row.append(grid[row_idx][c])
    print(','.join(output_row))
