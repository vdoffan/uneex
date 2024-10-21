import math

def main():
    seq = set(eval(input()))

    if not seq:
        print(0)
        return

    M = max(seq)
    if M < 3:
        print(0)
        return

    max_num = int(math.isqrt(M)) 
    squares = [i * i for i in range(1, max_num + 1)]

    sum_of_three_squares = set()
    n = len(squares)
    for i in range(n):
        s1 = squares[i]
        if s1 > M:
            break
        for j in range(i, n):
            s2 = s1 + squares[j]
            if s2 > M:
                break
            for k in range(j, n):
                s3 = s2 + squares[k]
                if s3 > M:
                    break
                sum_of_three_squares.add(s3)

    valid_numbers = sum_of_three_squares & seq

    print(len(valid_numbers))

if __name__ == "__main__":
    main()
