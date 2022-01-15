def fib(n):
    prev = 0
    curr = 1
    for i in range(n - 1):
        curr = curr + prev
        prev = curr
    return curr
