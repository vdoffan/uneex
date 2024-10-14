def squares(w, h, *args):
    screen = [['.' for _ in range(w)] for _ in range(h)]

    for square in args:
        X, Y, s, c = square
        for y in range(Y, Y + s):
            for x in range(X, X + s):
                if 0 <= x < w and 0 <= y < h:
                    screen[y][x] = c

    for row in screen:
        print(''.join(row))
