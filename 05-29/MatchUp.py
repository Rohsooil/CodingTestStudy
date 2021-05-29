"""
[[0,1],[2,3],[4,5],[6,7]]
[[0,1,2,3], [4,5,6,7]]

"""


def solution(n, a, b):
    match_list = []

    for i in range(0, n, 2):
        match_list.append([i, i + 1])

    answer = 0
    find = False
    while True:
        answer += 1
        for match in match_list:
            if (a - 1) in match and (b - 1) in match:
                find = True
                break
        if find:
            break
        match_list = []
        for i in range(0, n, 2 ** (answer + 1)):
            next_numbers = []
            for j in range(2 ** (answer + 1)):
                next_numbers.append(i + j)
            match_list.append(next_numbers)

    return answer


print(solution(8, 4, 7))
