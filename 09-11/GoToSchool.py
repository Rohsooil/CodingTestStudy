def solution(m, n, puddles):
    graph = [[0 for _ in range(n)] for _ in range(m)]

    for puddle in puddles:
        graph[puddle[0] - 1][puddle[1] - 1] = False

    graph[0][0] = 1

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            if graph[i][j] is False:
                continue

            if i == 0 or graph[i - 1][j] is False:
                graph[i][j] = (graph[i][j] + graph[i][j - 1]) % 1000000007
                continue
            elif j == 0 or graph[i][j - 1] is False:
                graph[i][j] = (graph[i][j] + graph[i - 1][j]) % 1000000007
                continue
            else:
                graph[i][j] = (graph[i][j] + graph[i - 1][j] + graph[i][j - 1]) % 1000000007

    answer = graph[m - 1][n - 1]
    return answer
