from collections import deque
import copy


def solution(info, edges):
    tree = {}
    visited = [False for _ in range(len(info))]

    for i in range(len(info)):
        tree[i] = {"value": info[i]}

    for edge in edges:
        if "left" in tree[edge[0]]:
            tree[edge[0]]["right"] = edge[1]
        else:
            tree[edge[0]]["left"] = edge[1]
        tree[edge[1]]["parent"] = edge[0]

    sheep = 0
    wolf = 0
    if tree[0]["value"] == 0:
        sheep += 1
    else:
        wolf += 1

    queue = deque([(0, sheep, wolf, [])])

    max_sheep = 0

    while queue:
        current, sheep, wolf, visited = queue.popleft()
        max_sheep = max(max_sheep, sheep)
        if current != 0 and current in visited:
            queue.append((tree[current]["parent"], sheep, wolf, copy.deepcopy(visited)))
            continue
        if current != 0:
            visited.append(current)
        if current in tree and "left" in tree[current]:
            left_node = tree[tree[current]["left"]]
            if left_node["value"] == 0:
                sheep += 1
                queue.append((tree[current]["left"], sheep, wolf, copy.deepcopy(visited)))
            else:
                if sheep > wolf + left_node["value"]:
                    wolf += 1
                    queue.append((tree[current]["left"], sheep, wolf, copy.deepcopy(visited)))

        if current in tree and "right" in tree[current]:
            right_node = tree[tree[current]["right"]]
            if right_node["value"] == 0:
                sheep += 1
                queue.append((tree[current]["right"], sheep, wolf, copy.deepcopy(visited)))
            else:
                if sheep > wolf + right_node["value"]:
                    wolf += 1
                    queue.append((tree[current]["right"], sheep, wolf, copy.deepcopy(visited)))

    answer = max_sheep
    return answer + 1


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
#
# print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
#                [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))
