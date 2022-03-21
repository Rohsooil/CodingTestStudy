def solution(board):
    memo = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if i == 0:
                memo[i][j] = board[i][j]
                continue
            if j == 0:
                memo[i][j] = board[i][j]
                continue
            if board[i][j] == 1:
                memo[i][j] = min(board[i][j] + memo[i - 1][j - 1], board[i][j] + memo[i][j - 1], board[i][j] + memo[i - 1][j])
    answer = 0
    for row in memo:
        answer = max(answer, max(row))
    return answer ** 2


print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))
print(solution([[0, 0, 1, 1], [1, 1, 1, 1]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 0]]))
print(solution([[0, 0, 0, 0], [0, 0, 0, 1]]))
print(solution([[1, 0, 0, 0]]))
print(solution([[0, 0, 0, 0]]))
print(solution([[0], [0], [0], [0]]))
print(solution([[0]]))
print(solution([[1]]))
