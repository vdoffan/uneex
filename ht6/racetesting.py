import itertools


def speed(path, stops, times):
    path_iter = iter(path)
    stops_iter = itertools.cycle(stops)
    times_iter = iter(times)
    while True:
        try:
            N = next(stops_iter)
        except StopIteration:
            break

        total_distance = 0
        for _ in range(N):
            try:
                distance = next(path_iter)
                total_distance += distance
            except StopIteration:
                break

        if total_distance == 0:
            break

        try:
            time = next(times_iter)
        except StopIteration:
            break

        average_speed = total_distance / time
        yield average_speed

