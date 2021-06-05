def solution(rows, columns, queries):
    matrix = []
    for i in range(rows):
        row_list = []
        start = columns * i + 1
        for j in range(columns):
            row_list.append(start + j)
        matrix.append(row_list)

    def rotate(query):
        min_num = 100 * 100 + 1
        start_point = (query[0] - 1, query[1] - 1)
        end_point = (query[2] - 1, query[3] - 1)

        current_num = matrix[start_point[0]][start_point[1]]
        next_num = 0
        for i in range(start_point[1], end_point[1]):
            min_num = min(min_num, current_num)
            next_num = matrix[start_point[0]][i + 1]
            matrix[start_point[0]][i + 1] = current_num
            current_num = next_num

        current_num = next_num
        for i in range(start_point[0], end_point[0]):
            min_num = min(min_num, current_num)
            next_num = matrix[i + 1][end_point[1]]
            matrix[i + 1][end_point[1]] = current_num
            current_num = next_num

        current_num = next_num
        for i in range(end_point[1], start_point[1], -1):
            min_num = min(min_num, current_num)
            next_num = matrix[end_point[0]][i - 1]
            matrix[end_point[0]][i - 1] = current_num
            current_num = next_num

        current_num = next_num
        for i in range(end_point[0], start_point[0], -1):
            min_num = min(min_num, current_num)
            next_num = matrix[i - 1][start_point[1]]
            matrix[i - 1][start_point[1]] = current_num
            current_num = next_num
        return min_num

    answer = []
    for query in queries:
        answer.append(rotate(query))

    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
