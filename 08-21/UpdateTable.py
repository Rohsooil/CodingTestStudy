def solution(n, k, cmd):
    linked_map = {0: [n - 1, 1], n - 1: [n - 2, 0]}
    deleted = []

    for i in range(1, n - 1):
        linked_map[i] = [i - 1, i + 1]
    for operation in cmd:
        if "U" in operation:
            up = int(operation.split()[-1])
            while up > 0:
                k = linked_map[k][0]
                up -= 1
        elif "D" in operation:
            down = int(operation.split()[-1])
            while down > 0:
                k = linked_map[k][1]
                down -= 1
        elif "C" in operation:
            now = linked_map[k]
            linked_map[now[0]][1] = now[1]
            linked_map[now[1]][0] = now[0]
            deleted.append((k, now))
            del linked_map[k]
            if not now[1]:
                k = now[0]
            else:
                k = now[1]
        elif "Z" in operation:
            if not deleted:
                continue
            idx, recovered = deleted.pop()
            linked_map[idx] = recovered
            linked_map[recovered[0]][1] = idx
            linked_map[recovered[1]][0] = idx

    answer = ['O' for _ in range(n)]
    for d in deleted:
        answer[d[0]] = 'X'

    return ''.join(answer)


""" 내가 했던 오답
def solution(n, k, cmd):
    deleted = []
    table = []
    first = 0
    last = n - 1

    for i in range(n):
        table.append("O")
    for operation in cmd:
        if "U" in operation:
            up = int(operation.split()[-1])
            while up > 0:
                k -= 1
                if table[k] == "X":
                    continue
                up -= 1
            if k <= first:
                k = first
        elif "D" in operation:
            down = int(operation.split()[-1])
            while down > 0:
                k += 1
                if table[k] == "X":
                    continue
                down -= 1
            if k >= last:
                k = last
        elif "C" in operation:
            table[k] = "X"
            deleted.append(k)

            if k == last:
                while table[k] == "X":
                    k -= 1
                    if k <= 0:
                        k = 0
                        break
                last = k
                continue
            k_first = False
            if k == first:
                k_first = True
            while table[k] == "X":
                k += 1
            if k_first:
                first = k
        elif "Z" in operation:
            if not deleted:
                continue
            recovered = deleted.pop()
            table[recovered] = "O"

            if recovered > last:
                last = recovered
            elif recovered < first:
                first = recovered

    print(first, last, k)
    answer = ''.join(table)
    return answer
"""


# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(8, 7, ["C", "C", "C", "C", "C", "C", "C", "C"]))
