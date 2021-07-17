"""
개발언어는 cpp, java, python 중 하나입니다.
직군은 backend, frontend 중 하나입니다.
경력은 junior, senior 중 하나입니다.
소울푸드는 chicken, pizza 중 하나입니다.
점수는 코딩테스트 점수를 의미하며, 1 이상 100,000 이하인 자연수입니다.
각 단어는 공백문자(스페이스 바) 하나로 구분되어 있습니다.

"""
from copy import deepcopy
from itertools import product


def solution(info_list, queries):
    person_map = {}
    init_list = [["cpp", "java", "python", "-"], ["backend", "frontend", "-"], ["junior", "senior", "-"], ["chicken", "pizza", "-"]]
    init_keys = product(init_list[0], init_list[1], init_list[2], init_list[3])
    for init_key in init_keys:
        person_map[' '.join(init_key)] = []

    for info in info_list:
        person_info = info.split()
        score = int(person_info[-1])
        other_info = []
        for i in range(4):
            with_any = ["-", person_info[i]]
            other_info.append(with_any)
        person_keys = product(other_info[0], other_info[1], other_info[2], other_info[3])
        for person_key in person_keys:
            person_map[' '.join(person_key)].append(score)

    for key in person_map.keys(): person_map[key].sort()

    def find_middle_idx(search_list, target):
        start, end = 0, len(search_list) - 1
        while start <= end:
            mid = (start + end) // 2
            if search_list[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        return len(search_list) - start

    answer = []
    for query in queries:
        match_count = 0
        query = query.replace(' and', '')
        conditions = query.split(' ')
        condition_score = int(conditions[-1])
        other_condition = ' '.join(conditions[:-1])

        if other_condition in person_map:
            match_count += find_middle_idx(person_map[other_condition], condition_score)
        answer.append(match_count)

    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
               ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]))
