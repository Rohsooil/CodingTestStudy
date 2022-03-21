from itertools import combinations


def solution(orders, course):
    answer = []

    for num in course:
        result_list = {}
        for order in orders:
            alphabet_list = list(order)
            alphabet_list.sort()
            alphabet_combinations = combinations(alphabet_list, num)

            # 딕서녀리에 조합된 알파벳을 키값으로, 빈도수를 값으로 넣음
            for element in alphabet_combinations:
                combined = ''.join(element)
                if combined in result_list:
                    result_list[combined] += 1
                else:
                    result_list[combined] = 1

        # 딕서녀리가 비어있지 않다면
        if result_list:

            # 최다 빈도수를 구함
            max_frequency = max(list(result_list.values()))

            # 최다 빈도수가 1이 아닐때, 최다 빈도수인 키를 정답 배열에 넣음
            if max_frequency != 1:
                for key in result_list.keys():
                    if result_list[key] == max_frequency:
                        answer.append(key)
    answer.sort()
    return answer


# counter 를 쓰는 방법도 있음


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
