from collections import deque


def solution(m, n, board):
    answer = 0
    list_board = [list(row) for row in board]

    while True:
        delete = set()
        for i in range(m - 1):
            for j in range(n - 1):
                now = list_board[i][j]
                if now == 0:
                    continue
                if list_board[i + 1][j] == now and list_board[i][j + 1] == now and list_board[i + 1][j + 1] == now:
                    delete.add((i, j))
                    delete.add((i + 1, j))
                    delete.add((i, j + 1))
                    delete.add((i + 1, j + 1))

        if not delete:
            break

        for i, j in delete:
            list_board[i][j] = 0
            answer += 1

        for i in range(n):
            queue = deque([])
            for j in range(m - 1, -1, -1):
                if list_board[j][i] == 0:
                    continue
                queue.append(list_board[j][i])
                list_board[j][i] = 0

            for j in range(m - 1, -1, -1):
                if queue:
                    list_board[j][i] = queue.popleft()

    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
print(solution(4, 5, ["AAAAA", "AUUUA", "AUUAA", "AAAAA"]))
print(solution(5, 6, ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]))
