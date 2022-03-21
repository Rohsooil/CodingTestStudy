def solution(n: int):
    return search([0] * n, 0)


def search(queen: list, row: int):
    n = len(queen)
    count = 0

    if n == row:
        return 1

    for col in range(n):
        queen[row] = col
        if check(queen, row):
            count += search(queen, row + 1)
    return count


def check(queen, row):
    for i in range(row):
        if queen[i] == queen[row] or abs(queen[i] - queen[row]) == row - i:
            return False

    return True
