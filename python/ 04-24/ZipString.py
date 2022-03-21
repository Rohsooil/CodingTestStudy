from collections import deque


def solution(s):
    answer = 1001

    for n in range(len(s) // 2 + 1):
        # n = 뽑을 숫자의 갯수
        result_str = ''
        qu = deque(list(s))
        stk = []
        while qu:
            cs = ''

            # queue 에서 n 개 만큼 뽑아서 문자열을 만듬
            for i in range(n + 1):
                if qu:
                    cs += qu.popleft()

            # (횟수, 문자열)
            # stack 이 비어있을경우 (0, 문자열)로 스택 첫 번째 값 지정
            if len(stk) == 0:
                stk.append((0, cs))

            # 스택에서 값을 뽑아옴
            stk_top = stk.pop()

            # 문자열이 스택에서 뽑아온것 과 같다면?
            if stk_top[1] == cs:
                # 스택에 횟수 + 1 하고 다시 넣음
                stk.append((stk_top[0] + 1, cs))
            else:
                # 아니면 차례로 스택에 집어넣음
                stk.append(stk_top)
                stk.append((1, cs))

        # 스택을 돌면서
        for elem in stk:
            # 횟수가 1을 초과하면 앞에 횟수를 붙여줌
            num = str(elem[0]) if elem[0] > 1 else ''
            result_str += num + elem[1]

        if len(result_str) < answer:
            answer = len(result_str)

    return answer


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
