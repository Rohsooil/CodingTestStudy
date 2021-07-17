def solution(arr):
    numbers_map = {0: 0, 1: 0}
    maximum = len(arr) * len(arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            numbers_map[arr[i][j]] += 1

    if numbers_map[0] == maximum:
        return [1, 0]

    if numbers_map[1] == maximum:
        return [0, 1]

    def quad_zip(first, length):
        if length == 1:
            return
        all_same = True
        first_number = arr[first[0]][first[1]]
        for i in range(first[0], first[0] + length):
            for j in range(first[1], first[1] + length):
                if arr[i][j] != first_number:
                    all_same = False
                    break
            if not all_same:
                break

        if all_same:
            numbers_map[first_number] -= length * length - 1
        else:
            next_length = length // 2
            quad_zip((first[0], first[1] + next_length), next_length)
            quad_zip((first[0] + next_length, first[1]), next_length)
            quad_zip((first[0], first[1]), next_length)
            quad_zip((first[0] + next_length, first[1] + next_length), next_length)

    quad_zip((0, 0), len(arr))
    answer = [numbers_map[0], numbers_map[1]]
    return answer


print(solution([[1, 1, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1]]))

print(solution([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]))

print(solution([[1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 1, 1, 1, 1]]))
