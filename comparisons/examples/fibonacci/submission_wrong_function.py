"""
Your task is to create a function called fib that produces the nth Fibonacci number, where fib(0) = 0 and fib(1) = 1.
"""


def fib(n):
    out = 1
    for i in range(n):
        out *= i
    return out
