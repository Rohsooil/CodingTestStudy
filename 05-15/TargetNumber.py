answer = 0


def solution(numbers, target):

    def dfs(sum_of, position):
        if position == len(numbers):
            if sum_of == target:
                global answer
                answer += 1
            return
        dfs(sum_of + numbers[position], position + 1)
        dfs(sum_of - numbers[position], position + 1)

    dfs(0, 0)
    return answer
