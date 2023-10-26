def rhombus_logic(row, n):
    print(" " * (n - row), end="")
    print(*["*"] * row)


def rhombus_up(n):
    for row in range(1, n + 1):
        rhombus_logic(row, n)


def rhombus_down(n):
    for row in range(n - 1, 0, -1):
        rhombus_logic(row, n)


def rhombus_finalized(n):
    rhombus_up(n)
    rhombus_down(n)


num = int(input())

rhombus_finalized(num)