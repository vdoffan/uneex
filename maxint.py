def is_int(some_str):
    try:
        if some_str.startswith('+'):
            raise
        num = int(some_str)
        return (True, num)
    except:
        return (False, -1)

def main():
    max_int = 0
    was_int = False
    while str := input():
        for elem in str.split(' '):
            fl = is_int(elem)
            if fl[0]:
                if not was_int:
                    max_int = fl[1]
                    was_int = True
                else:
                    max_int = max(max_int, fl[1])
    print(max_int)

if __name__ == '__main__':
    main()