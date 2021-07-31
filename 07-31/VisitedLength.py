def solution(dirs):
    dir_dict = {'U': (1, 0), 'D': (-1, 0), 'R': (0, 1), 'L': (0, -1)}

    now = (5, 5)
    visit_map = {}
    answer = 0
    for direction in dirs:
        next_add = dir_dict[direction]
        if now[0] + next_add[0] > 10 or now[0] + next_add[0] < 0 or now[1] + next_add[1] > 10 or now[1] + next_add[1] < 0:
            continue

        key = ','.join(map(str, now))
        now = (now[0] + next_add[0], now[1] + next_add[1])
        now_key = ','.join(map(str, now))

        if key + '->' + now_key not in visit_map and now_key + '->' + key not in visit_map:
            answer += 1
            visit_map[key + '->' + now_key] = 1
            visit_map[now_key + '->' + key] = 1

    return answer


print(solution("LLLLLLLLL"))
print(solution("RRRRRRRRR"))
print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
