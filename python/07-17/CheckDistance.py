from collections import deque


def solution(places):
    MAX_LENGTH = 5
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]

    def in_manhattan_distance(now, other):
        height_gap = abs(now[0] - other[0])
        width_gap = abs(now[1] - other[1])
        if height_gap + width_gap > 2:
            return False
        return True

    def check_placed(place):
        keeping = True
        queue = deque([])
        for i in range(MAX_LENGTH):
            for j in range(MAX_LENGTH):
                if place[i][j] == 'P':
                    queue.append((i, j))
        while queue:
            start = queue.popleft()
            inner_queue = deque([start])
            visited = [[False for _ in range(5)] for _ in range(5)]
            while inner_queue:
                y, x = inner_queue.popleft()
                visited[y][x] = True
                for i in range(4):
                    next_y, next_x = y + dy[i], x + dx[i]
                    if next_y >= MAX_LENGTH or next_y < 0 or next_x >= MAX_LENGTH or next_x < 0 or place[next_y][next_x] == 'X' or visited[next_y][next_x]:
                        continue
                    if not in_manhattan_distance(start, (next_y, next_x)):
                        continue
                    if place[next_y][next_x] == 'P':
                        keeping = False
                        break
                    inner_queue.append((next_y, next_x))
            if not keeping:
                break
        return keeping

    answer = []
    for element in places:
        place_list = [list(row) for row in element]
        check = check_placed(place_list)
        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([["POOOP",
                 "OXXOX",
                 "OPXPX",
                 "OOXOX",
                 "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

print(solution([["POPOO",
                 "OOOOO",
                 "OOOOO",
                 "OOOOO",
                 "OOOOO"]]))
#
# print(solution([["OOOOO",
#                  "OOOOO",
#                  "OOOOO",
#                  "OOPOP",
#                  "OOOPP"]]))
#
# print(solution([["PXOXP",
#                  "XPXPX",
#                  "OXPXO",
#                  "XPXPX",
#                  "PXOXP"]]))
