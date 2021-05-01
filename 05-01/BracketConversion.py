"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.
"""


def solution(p):
    # 올바른 괄호 문자열인지 판별
    def right_bracket(bracket):
        b_list = list(bracket)
        tmp_list = []  # 임시 스택

        for b in b_list:
            # 스택 탑이 ( 이고 현재 문자열이 ) 이라면 스택에서 꺼냄 아니면 집어넣음
            if tmp_list and (b == ')' and tmp_list[-1] == '('):
                tmp_list.pop()
            else:
                tmp_list.append(b)
        # 스택이 비어있지 않으면 괄호가 전부 닫혀있지 않은 상태임
        if tmp_list:
            return False
        return True

    # u, v 를 나눔
    def divide_u_v(u_v):
        open = 0
        close = 0
        u_bracket = ''
        v_bracket = u_v

        # ( 와 ) 갯수가 같아질 때 까지 u 에다가 집어넣음 나머지는 v
        for i in range(len(u_v)):
            if '(' == u_v[i]:
                open += 1
            elif ')' == u_v[i]:
                close += 1

            u_bracket += u_v[i]
            v_bracket = u_v[i + 1:len(u_v)]
            if open == close:
                break
        return u_bracket, v_bracket

    def recurse(s):
        # 문자열이 비어있거나 올바른 괄호라면 그대로 반환
        if not s or s == '' or right_bracket(s):
            return s

        u, v = divide_u_v(s)

        # u 가 올바른 괄호라면 v 를 재귀한 것과 합쳐서 리턴 아니면 문제의 조건대로 작업 수행
        if right_bracket(u):
            return u + recurse(v)
        else:
            tmp_v = '(' + recurse(v) + ')'
            tmp_u = ''

            for i in range(1, len(u) - 1):
                if u[i] == '(':
                    tmp_u += ')'
                elif u[i] == ')':
                    tmp_u += '('

            return tmp_v + tmp_u

    return recurse(p)


# print(solution("(()())()"))
# print(solution(")("))
print(solution("()))((()"))
