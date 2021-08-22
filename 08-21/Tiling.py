def solution(n):
    memo = [1, 2]

    if n == 1:
        return 1

    if n == 2:
        return 2

    for i in range(2, n):
        memo.append((memo[i - 1] + memo[i - 2]) % 1000000007)

    return memo[-1]


print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
