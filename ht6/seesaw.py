def seesaw(sequence):
    even = []
    odd = []

    for i in sequence:
        if not i % 2:
            even.append(i)
        else:
            odd.append(i)

    i = 0
    while i < max(len(even), len(odd)):
        if i < len(even):
            yield even[i]
        if i < len(odd):
            yield odd[i]
        i += 1
