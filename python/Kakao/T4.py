import copy


def solution(n, info):
    rion = [0 for _ in range(11)]

    def compare_list(list1, list2):
        for i in range(10, -1, -1):
            if list1[i] < list2[i]:
                return list2
        return list1

    def rion_can_win():
        rion_score = 0
        apeach_score = 0
        for i in range(11):
            if rion[i] > info[i]:
                rion_score += 10 - i
            else:
                apeach_score += 10 - i
        return rion_score > apeach_score

    result_list = []

    def dfs(current):
        if sum(rion) == n:
            if rion_can_win():
                result_list.append(copy.deepcopy(rion))
            return
        for j in range(current, 11):
            rion[i] += 1
            dfs(current)
            rion[i] -= 1

    for i in range(11):
        dfs(i)
    answer = [-1]
    for result in result_list:
        if not answer:
            answer = result
        else:
            answer = compare_list(answer, result)

    return answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
# print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
