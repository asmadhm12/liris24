def fibonacci(n):
    """
    Calculate the n-th Fibonacci number.

    :param n: An integer, the position in the Fibonacci sequence.
    :return: The n-th Fibonacci number.
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b