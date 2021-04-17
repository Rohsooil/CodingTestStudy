def solution(numbers):
    answer = []

    # 배열 길이 만큼 반복
    for i in range(len(numbers)):
        # numbers[0] + numbers[1] = numbers[1] + numbers[0] 이므로
        # j 값을 i + 1 부터 반복해서 다 더함
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])

    # set 을 이용해서 중복 제거하고 sort
    answer = list(set(answer))
    answer.sort()
    return answer


print(solution([2, 1, 3, 4, 1]))
