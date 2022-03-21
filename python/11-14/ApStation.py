import math


def solution(n, stations, w):
    empty_list = []
    answer = 0

    if stations[0] - w - 1 >= 1:
        empty_list.append([1, stations[0] - w - 1])

    for i in range(len(stations) - 1):
        start = stations[i] + w + 1
        end = stations[i + 1] - w - 1
        if start <= end:
            empty_list.append([start, end])

    if stations[-1] + w + 1 <= n:
        empty_list.append([stations[-1] + w + 1, n])

    for empty in empty_list:
        length = empty[1] - empty[0] + 1
        if length <= w * 2 + 1:
            answer += 1
        else:
            answer += math.ceil(length / (w * 2 + 1))

    return answer
