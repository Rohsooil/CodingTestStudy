def solution(id_list, report, k):
    id_map = {}

    for id in id_list:
        id_map[id] = {"report_from": set(), "report_who": set()}

    for data in report:
        user, reported = data.split(' ')
        id_map[user]["report_who"].add(reported)
        id_map[reported]["report_from"].add(user)

    banned_list = set()
    for key in id_map.keys():
        if len(id_map[key]["report_from"]) >= k:
            banned_list.add(key)

    answer = []

    for id in id_list:
        notified = 0
        for banned in banned_list:
            if banned in id_map[id]["report_who"]:
                notified += 1
        answer.append(notified)

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))

print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"]	, 3))
