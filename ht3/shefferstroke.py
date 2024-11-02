def sheff(A, B):
    if not A and not B:
        return True
    elif bool(A) != bool(B):
        return A if A else B
    else:
        return False