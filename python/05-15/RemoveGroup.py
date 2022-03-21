def solution(s):
    stack = []

    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    answer = 0

    if stack:
        answer = 0
    else:
        answer = 1

    return answer
