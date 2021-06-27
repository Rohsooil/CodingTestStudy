import heapq


def solution(N, road, K):
    MAX_NUM = 50001
    distance = [MAX_NUM] * (N + 1)
    road_list = [[] for _ in range(N + 1)]

    for line in road:
        a = line[0]
        b = line[1]
        c = line[2]
        if c > K:
            continue
        road_list[a].append((b, c))
        road_list[b].append((a, c))

    answer = 0

    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for dot in road_list[now]:
                cost = dist + dot[1]
                if cost < distance[dot[0]]:
                    distance[dot[0]] = cost
                    heapq.heappush(q, (cost, dot[0]))

    dijkstra(1)
    for i in range(N + 1):
        if distance[i] <= K:
            answer += 1

    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
