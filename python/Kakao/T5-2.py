import heapq


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        graph[edge[0]].append((edge[1], 1))
        graph[edge[1]].append((edge[0], 1))

    distance = [1001] * len(info)

    def dijkstra(start):
        q = []

        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for dot in graph[now]:
                cost = dist + dot[1]
                if cost < distance[dot[0]]:
                    distance[dot[0]] = cost
                    heapq.heappush(q, (cost, dot[0]))

    dijkstra(0)
    print(distance)

    return None


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
