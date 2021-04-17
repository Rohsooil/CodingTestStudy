"""

0   1   3
0 2 5   1
0 2 4 4 2
3 5 1 3 1


1 5 3 5 1 2 1 4
"""


def solution(board, moves):
    stack = []
    answer = 0

    # moves 순서대로
    for i in moves:

        doll = 0
        for row in board:
            # 배열의 빈 공간 pass
            if row[i - 1] == 0:
                continue
            # 비어있지 않으면 뽑아서 doll 에 저장
            else:
                doll = row[i - 1]
                row[i - 1] = 0
                break

        if doll == 0:
            continue

        # 스택이 비어있으면 그냥 append
        if len(stack) == 0:
            stack.append(doll)
        # 아니면 top 을 먼저 뽑아보고
        else:
            top_of_stack = stack.pop()
            # top != doll 이면 둘다 스택에 다시 집어넣음 (doll 이 위로 가게)
            if top_of_stack != doll:
                stack.append(top_of_stack)
                stack.append(doll)
            # 아니라면 집어넣을 필요가 없음, 터진 횟수 +1
            else:
                answer = answer + 1
    # 사라진 인혀의 갯수 = 터진횟수 * 2
    return answer * 2


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))
