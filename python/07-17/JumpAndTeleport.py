def solution(n):
    answer = 1
    if n == 1 or n == 2:
        return 1

    while n != 1:
        share = n // 2
        remainder = n % 2
        if remainder == 1:
            answer += 1
        n = share

    return answer


print(solution(1))
print(solution(6))
print(solution(5))
print(solution(8))
