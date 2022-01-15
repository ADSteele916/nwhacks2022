def fm(n):
    return fm(n-1)+fm(n-2) if n > 1 else n