def reverse_text(string):
    current = len(string) - 1
    end = 0

    while current >= end:
        yield string[current]
        current -= 1
