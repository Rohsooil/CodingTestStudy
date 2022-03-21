def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer


# 조합으로 처음에 접근했으나 시간초과...
# def solution(number, k):
#     combi_list = combinations(number, len(number) - k)
#     answer = ''.join(max(combi_list))
#     return answer


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
