def solution(n):
    memo = []

    for i in range(n):
        if i == 0:
            memo.append(1)
        elif i == 1:
            memo.append(2)
        else:
            next_case = (memo[i - 2] + memo[i - 1]) % 1234567
            memo.append(next_case)

    return memo[-1]
