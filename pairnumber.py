lines = []
while True:
    line = input().strip()
    if line == '':
        break
    lines.append(line)

words = ' '.join(lines).split()

unique_pairs = set()

for i in range(len(words) - 1):
    pair = tuple(sorted([words[i], words[i + 1]]))
    unique_pairs.add(pair)

print(len(unique_pairs))
