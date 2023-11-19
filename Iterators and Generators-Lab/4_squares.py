def squares(n):
    current = 1
    while current <= n:
        yield current * current
        current += 1

