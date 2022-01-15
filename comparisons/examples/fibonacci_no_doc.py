def fib(n: int) -> int:
    if n < 0:
        raise ValueError()
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for i in range(n - 1):
        curr, prev = curr + prev, curr
    return curr
