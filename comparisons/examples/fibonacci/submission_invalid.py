"""
Your task is to create a function called fib that produces the nth Fibonacci number, where fib(0) = 0 and fib(1) = 1.
"""


def fib(n):
    """Computes the Fibonacci number with the given index"""
    prev = 0
    curr = 1
    for i in range(n - 1):
        curr = curr + prev
        prev = curr
    return curr
