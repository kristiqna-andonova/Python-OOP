def fibonacci():
    current_n, next_n = 0, 1
    while True:
        yield current_n
        current_n, next_n = next_n, current_n + next_n
