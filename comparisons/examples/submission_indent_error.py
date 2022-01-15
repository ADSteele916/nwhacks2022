"""
Your task is to create a function called fib that produces the nth Fibonacci number, where fib(0) = 0 and fib(1) = 1.
"""


def fib(n: int) -> int:
    """Computes the nth Fibonacci number.

    Args:
        n: index to compute.

    Returns:
        Fibonacci number with the given index.

    Raises:
        ValueError: Given a negative index.
    """
    if n < 0:
        raise ValueError("Cannot compute a negative Fibonacci number.")
    if n <= 1:
        return n
     prev = 0
    curr = 1
    for i in range(n - 1):
        curr, prev = curr + prev, curr
    return curr
