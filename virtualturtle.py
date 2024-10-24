def turtle(coord, direction):
    x, y = coord
    dir = direction

    possible_moves = {
        0: (1, 0),
        1: (0, 1),
        2: (-1, 0),
        3: (0, -1)
    }

    while True:
        command = yield (x, y)

        if command == 'f':
            x += possible_moves[dir][0]
            y += possible_moves[dir][1]

        elif command == 'l':
            dir = (dir + 1) % 4

        elif command == 'r':
            dir = (dir - 1) % 4

        else:
            continue
