"""
Your task is to create a function called fib that produces the nth Fibonacci number, where fib(0) = 0 and fib(1) = 1.
"""


def fib(n):
    """Computes the nth Fibonacci number"""
    return fib(n-1)+fib(n-2) if n > 1 else n
