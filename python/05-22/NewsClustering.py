import re


def solution(str1, str2):
    def collect_string(str_):
        str_ = str_.lower()
        str_list = []
        for i in range(len(str_) - 1):
            s = str_[i] + str_[i + 1]

            if not re.match(r'[a-zA-Z]+$', s):
                continue
            else:
                str_list.append(s)
        return str_list

    collect_1 = collect_string(str1)
    collect_2 = collect_string(str2)

    if not collect_1 and not collect_2:
        return 65536

    intersection = []
    union = collect_1 + collect_2
    for i in range(len(collect_1)):
        for j in range(len(collect_2)):
            if collect_2[j] and collect_1[i] == collect_2[j]:
                intersection.append(collect_2[j])
                union.remove(collect_2[j])
                collect_2[j] = False
                break

    answer = int(len(intersection) / len(union) * 65536)
    return answer


"""
2 aa aa aa
1 aa aa

"""

print(solution('FRANCE', 'french'))
print(solution('FrANCE', 'zxcv'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2	', 'AAAA12'))
print(solution('E=M*C^2	', 'e=m*c^2	'))
