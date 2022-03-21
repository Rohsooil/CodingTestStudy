from collections import deque


def solution(n):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    direction = [(1, 0), (0, 1), (-1, -1)]

    now = 1
    graph[0][0] = now
    queue = deque([(0, 0)])
    now_direction = 0
    while queue:
        now_y, now_x = queue.popleft()
        next_y, next_x = now_y + direction[now_direction][0], now_x + direction[now_direction][1]
        if next_y >= n or next_x >= n or graph[next_y][next_x] != 0:
            now_direction = (now_direction + 1) % 3
        next_y, next_x = now_y + direction[now_direction][0], now_x + direction[now_direction][1]
        if next_y >= n or next_x >= n or graph[next_y][next_x] != 0:
            break
        now += 1
        graph[next_y][next_x] = now
        queue.append((next_y, next_x))

    answer = []

    for row in graph:
        for num in row:
            if num != 0:
                answer.append(num)
    return answer


"1 0 0 0"
"2 9 0 0"
"3 10 8 0"
"4 5 6 7"

print(solution(4))
