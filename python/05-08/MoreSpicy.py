import heapq


# 최소 힙을 이용하여 접근!
def solution(scoville, K):
    # 스코빌 계산
    def mix(num1, num2):
        return num1 + (num2 * 2)

    # 최소 힙으로 만들고
    heapq.heapify(scoville)
    answer = 0
    # 최소값이 K 보다 작다면
    while scoville[0] < K:
        min_num = heapq.heappop(scoville)

        # K 보다 작은거 두개를 꺼내야하는데 하나만 꺼낼수 있으면 불가능
        if len(scoville) == 0:
            return -1
        next_min_num = heapq.heappop(scoville)

        new_scov = mix(min_num, next_min_num)
        heapq.heappush(scoville, new_scov)

        answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2], 7))
