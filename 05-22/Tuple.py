def solution(s):
    numbers = []
    tuples = []
    opened = False
    number = ''
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            opened = True
        elif s[i] == ',':
            if opened:
                numbers.append(int(number))
                number = ''
        elif s[i] == '}':
            opened = False
            numbers.append(int(number))
            number = ''
            tuples.append(numbers)
            numbers = []
        else:
            number += s[i]

    tuples.sort(key=len)

    answer = []
    for elements in tuples:
        for element in elements:
            if element not in answer:
                answer.append(element)
                break

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
