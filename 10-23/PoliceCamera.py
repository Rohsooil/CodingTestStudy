def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])
    for route in routes:
        route.append(False)

    for i in range(len(routes)):
        if not routes[i][2]:
            first = routes[i]
            answer += 1
        for j in range(i + 1, len(routes)):
            if routes[j][2]:
                continue
            if routes[j][0] <= first[1] <= routes[j][1]:
                routes[j][2] = True

    return answer
