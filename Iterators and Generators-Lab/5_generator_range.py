def genrange(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

