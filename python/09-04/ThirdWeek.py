from collections import deque


def solution(game_board, table):
    def rotate():
        temp_table = [[0 for _ in range(len(game_board[0]))] for _ in range(len(game_board))]
        for _i in range(len(game_board)):
            for _j in range(len(game_board[0])):
                temp_table[_j][len(game_board) - 1 - _i] = game_board[_i][_j]
        return temp_table

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    shape_list = []

    for i in range(len(table)):
        for j in range(len(table[0])):
            if table[i][j] == 0:
                continue

            max_y, max_x, min_y, min_x = 0, 0, len(table), len(table[0])
            shape_queue = deque([(i, j)])
            shape = []
            while shape_queue:
                y, x = shape_queue.popleft()
                max_y, max_x, min_y, min_x = max(max_y, y), max(max_x, x), min(min_y, y), min(min_x, x)
                table[y][x] = 0
                shape.append((y, x))
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]

                    if nx < 0 or ny < 0 or nx >= len(table[0]) or ny >= len(table):
                        continue
                    if table[ny][nx] == 1:
                        shape_queue.append((ny, nx))

            for row in shape:
                row[0] = row[0] - min_y
                row[1] = row[1] - min_x

            temp = [[0 for _ in range(max_x - min_x)] for _ in range(max_y - min_y)]

            for row in shape:
                temp[row[0]][row[1]] = 1
            shape_list.append(temp)

    answer = 0
    for t in range(4):
        for i in range(len(game_board)):
            for j in range(len(game_board[0])):
                if game_board[i][j] == 1:
                    continue
                min_y, min_x = len(game_board), len(game_board[0])
                shape_queue = deque([(i, j)])
                shape = []
                while shape_queue:
                    y, x = shape_queue.popleft()
                    min_y, min_x = min(min_y, y), min(min_x, x)
                    table[y][x] = 0
                    shape.append((y, x))
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if nx < 0 or ny < 0 or nx >= len(table[0]) or ny >= len(table):
                            continue
                        if table[ny][nx] == 1:
                            shape_queue.append((ny, nx))
                    for row in shape:
                        row[0] = row[0] - min_y
                        row[1] = row[1] - min_x
                    shape.sort()
        game_board = rotate()

    for row in game_board:
        print(row)
    return answer


print(solution([[1, 1, 0, 0, 1, 0],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 0, 0]],
               [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 0, 0]]))
