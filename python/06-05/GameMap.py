from collections import deque


def solution(maps):
    queue = deque()
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    start = (0, 0)
    queue.append(start)
    m = len(maps)
    n = len(maps[0])
    while queue:
        (x, y) = queue.popleft()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if next_x == 0 and next_y == 0:
                continue

            if next_x < 0 or next_y < 0 or next_x >= n or next_y >= m:
                continue

            if maps[next_y][next_x] == 1:
                maps[next_y][next_x] = maps[y][x] + 1
                queue.append((next_x, next_y))

    if maps[m - 1][n - 1] == 1:
        return -1

    return maps[m - 1][n - 1]


print(solution([[1, 0, 1, 1, 1]]))
print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
