import math

def distance(galaxy1, galaxy2):
    x1, y1, z1 = galaxy1[0], galaxy1[1], galaxy1[2]
    x2, y2, z2 = galaxy2[0], galaxy2[1], galaxy2[2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

galaxies = []
while True:
    line = input().strip()
    if ' ' not in line:
        break
    x, y, z, name = line.split()
    galaxies.append(((float(x), float(y), float(z)), name))

max_distance = -1
galaxy_pair = ('', '')

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        galaxy1, name1 = galaxies[i]
        galaxy2, name2 = galaxies[j]
        dist = distance(galaxy1, galaxy2)
        if dist > max_distance:
            max_distance = dist
            galaxy_pair = (name1, name2)

print(' '.join(sorted(galaxy_pair)))
