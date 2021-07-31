from collections import deque


def solution(msg):
    dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                  "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
                  "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
    next_num = 27
    answer = []
    idx = 0
    while idx < len(msg):
        check = ''
        queue = deque(list(msg[idx:]))
        while queue:
            next_ch = queue.popleft()
            if check + next_ch in dictionary:
                check += next_ch
                idx += 1
                continue
            else:
                dictionary[check + next_ch] = next_num
                answer.append(dictionary[check])
                next_num += 1
                break
        if idx >= len(msg) and check:
            answer.append(dictionary[check])

    return answer


print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))
