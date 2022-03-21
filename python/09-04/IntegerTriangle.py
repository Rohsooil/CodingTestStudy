def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(0, i + 1):
            if j == 0:
                triangle[i][j] = triangle[i - 1][j] + triangle[i][j]
                continue

            if j == i:
                triangle[i][j] = triangle[i - 1][j - 1] + triangle[i][j]
                continue

            left = triangle[i - 1][j - 1] + triangle[i][j]
            right = triangle[i - 1][j] + triangle[i][j]

            if left > right:
                triangle[i][j] = left
            else:
                triangle[i][j] = right

    answer = 0
    for i in range(len(triangle)):
        answer = max(triangle[len(triangle) - 1][i], answer)

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
