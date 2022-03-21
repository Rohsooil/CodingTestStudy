from collections import deque


def solution(board):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    answer = 500 * len(board) * len(board)
    queue = deque([(0, 0, 0, None)])
    visited = {}
    while queue:
        y, x, cost, direction = queue.popleft()
        if y == len(board) - 1 and x == len(board) - 1:
            answer = min(answer, cost)
            continue

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            new_cost = cost
            if ny < 0 or nx < 0 or ny >= len(board) or nx >= len(board):
                continue

            if board[ny][nx] == 1:
                continue

            if direction is not None:
                if direction == 'Y' and dy[i] == 0:
                    new_cost += 500 + 100
                elif direction == 'X' and dx[i] == 0:
                    new_cost += 500 + 100
                else:
                    new_cost += 100
            else:
                new_cost += 100

            next_direction = 'Y' if dx[i] == 0 else 'X'

            if (ny, nx, next_direction) in visited and visited[(ny, nx, next_direction)] <= new_cost:
                continue

            visited[(ny, nx, next_direction)] = new_cost
            queue.append((ny, nx, new_cost, next_direction))
    return answer
