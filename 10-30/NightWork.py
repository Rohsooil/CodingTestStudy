import heapq


def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, -work)

    heapq.heapify(heap)
    answer = 0

    for i in range(n):
        maximum = heapq.heappop(heap)
        maximum += 1
        if maximum > 0:
            maximum = 0
        heapq.heappush(heap, maximum)

    for element in heap:
        answer += element * element

    if answer < 0:
        return 0

    return answer