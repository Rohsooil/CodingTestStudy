def solution(n, results):
    answer = 0
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(len(results)):
        win = results[i][0] - 1
        lose = results[i][1] - 1
        graph[win][lose] = 1
        graph[lose][win] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or graph[i][j] != 0:
                    continue
                if graph[i][k] == graph[k][j]:
                    graph[i][j] = graph[i][k]

    for i in range(n):
        flag = True
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] == 0 and graph[j][i] == 0:
                flag = False
                break
        if flag:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
