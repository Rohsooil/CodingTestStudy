import re


def solution(s):
    def change(binary_str, removed, repeat):
        repeat += 1
        removed += len(re.findall("0", binary_str))
        binary_str = binary_str.replace("0", "")
        length_of_str = len(binary_str)
        binary_length = format(length_of_str, "b")
        if binary_length == "1":
            return removed, repeat
        return change(binary_length, removed, repeat)

    result_removed, result_repeat = change(s, 0, 0)
    answer = [result_repeat, result_removed]
    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
