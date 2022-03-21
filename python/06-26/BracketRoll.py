def solution(s):
    def right_bracket(brackets):
        stack = []
        for i in range(len(brackets)):
            if not stack:
                stack.append(brackets[i])
            elif stack[-1] == '[' and brackets[i] == ']':
                stack.pop()
            elif stack[-1] == '{' and brackets[i] == '}':
                stack.pop()
            elif stack[-1] == '(' and brackets[i] == ')':
                stack.pop()
            else:
                stack.append(brackets[i])
        if stack:
            return False
        return True

    answer = 0
    for i in range(len(s)):
        if right_bracket(s):
            answer += 1
        first_bracket = s[0]
        s = s[1:]
        s += first_bracket

    return answer


print(solution("[](){}"))
print(solution("}]()[{"))
print(solution("[)(]"))
