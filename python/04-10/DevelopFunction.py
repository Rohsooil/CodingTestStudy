def solution(progresses, speeds):
    answer = []
    # 다음 첫 번째 작업 번호
    next_seq = 0

    # 다음 첫 번째 작업 번호가 배열 안에 존재할 때 까지
    while next_seq < len(progresses):
        # 다음 배포까지 걸린 일
        numbers = 0

        # 작업 배열에 각 인덱스에 해당하는 speed 를 더함
        for i in range(next_seq, len(progresses)):
            progresses[i] = progresses[i] + speeds[i]

        # 다음 첫 번 쨰 작업부터 배열을 돌면서
        for i in range(next_seq, len(progresses)):
            # 100% 완료 된 작업까지 반복
            if progresses[i] >= 100:
                next_seq = i + 1
                numbers = numbers + 1
            else:
                break

        # 걸린 일수가 0 이 아니라면 정답 배열에 append
        if numbers != 0:
            answer.append(numbers)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
