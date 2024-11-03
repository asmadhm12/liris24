def factorielle(n):
    """Cadlcule la factorielle de n (n!)."""
    if n < 0:
        raise ValueError("Le nombre doit être non-négatif")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
