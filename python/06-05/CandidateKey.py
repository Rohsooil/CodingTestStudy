from itertools import combinations


def solution(relations):
    count = len(relations)
    columns = []
    for i in range(len(relations[0])):
        columns.append(i)
    check_minimal_list = []

    def count_rows(column_combination):
        group = {}
        for row in relations:
            key_name = ''
            for column in column_combination:
                key_name += row[column]

            if key_name in group:
                group[key_name] += 1
            else:
                group[key_name] = 1
        return len(group.keys())

    def mininal(check_key_list):
        for minial_list in check_minimal_list:
            if set(minial_list).issubset(set(check_key_list)):
                return False
        return True

    answer = 0
    for i in range(1, len(relations[0]) + 1):
        key_combination = combinations(columns, i)
        for keys in key_combination:
            key_list = list(keys)
            if not mininal(key_list):
                continue
            if count == count_rows(key_list):
                check_minimal_list.append(key_list)
                answer += 1

    return answer


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"],
                ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
