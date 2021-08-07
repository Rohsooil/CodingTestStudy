def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == '(' and ch == ')':
            stack.pop()
        else:
            stack.append(ch)

    answer = True
    if stack:
        answer = False
    return answer


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))
