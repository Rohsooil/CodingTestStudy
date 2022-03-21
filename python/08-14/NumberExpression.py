def solution(n):
    answer = 0
    memo = 0
    start = 1
    i = 1
    while start < n:
        memo += i
        if memo == n:
            answer += 1
            memo = 0
            start += 1
            i = start
        elif memo > n:
            memo = 0
            start += 1
            i = start
        i += 1

    return answer
