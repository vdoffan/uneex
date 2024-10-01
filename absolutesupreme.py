def triple_max(a, b):
    a_s = sorted(a)
    b_s = sorted(b)
    for i in range(3):
        if a_s[i] > b_s[i]:
            return False
    return a_s != b_s

def build_relation(arr):
    n = len(arr)
    relation = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                relation[i][j] = triple_max(arr[i], arr[j])
    return relation

def topological_sort(arr):
    n = len(arr)
    relation = build_relation(arr)
    processed = set()
    for _ in range(n):
        min_out_edges = n
        k = -1
        for i in range(n):
            if i not in processed:
                out_edges = sum(relation[i][j] for j in range(n) if j != i)
                if out_edges < min_out_edges:
                    min_out_edges = out_edges
                    k = i
        if k == -1:
            break
        print(', '.join(map(str, arr[k])))
        processed.add(k)
        for i in range(n):
            relation[i][k] = False

if __name__ == "__main__":
    arr = []
    try:
        while True:
            s = input()
            if not s.strip():
                break
            arr.append(tuple(map(int, s.strip().split(','))))
    except EOFError:
        pass
    topological_sort(arr)
