def solution(n, build_frame):
    answer = set()

    def valid():
        for x, y, a in answer:
            # 0 기둥
            if a == 0:
                # 바로 밑에 기둥이 있거나 왼쪽 칸이 보이거나 현재 좌표에 보가 있거나 맨 땅인경우 오케이
                if (x, y - 1, 0) in answer or (x - 1, y, 1) in answer or (x, y, 1) in answer or y == 0:
                    continue
                else:
                    return False
            # 1 보
            if a == 1:
                # 바로 밑에 기둥이 있거나 (왼쪽 끝) 오른쪽 끝이 기둥이거나 양 끝이 보로 되어있는 경우 오케이
                if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                    continue
                else:
                    return False
        return True

    for element in build_frame:
        e_x, e_y, tp, method = element

        # 0 삭제
        if method == 0:
            answer.remove((e_x, e_y, tp))
            if not valid():
                answer.add((e_x, e_y, tp))
        # 1 설치
        else:
            answer.add((e_x, e_y, tp))
            if not valid():
                answer.remove((e_x, e_y, tp))

    answer = [list(i) for i in answer]
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer
