import heapq


def solution(n, s, a, b, fares):
    s = s - 1
    a = a - 1
    b = b - 1

    graph = [[] for _ in range(n)]
    for fare in fares:
        src, dst, cst = fare[0] - 1, fare[1] - 1, fare[2]
        graph[src].append((dst, cst))
        graph[dst].append((src, cst))

    def dijkstra(start, destination):
        q = []
        heapq.heappush(q, (0, start))
        distance = [n * 1000000 for _ in range(n)]
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

        return distance[destination]

    answer = dijkstra(s, a) + dijkstra(s, b)
    for i in range(0, n):
        if s != i:
            answer = min(answer, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
