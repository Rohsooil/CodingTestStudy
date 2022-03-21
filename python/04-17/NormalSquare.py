def greatest_common_factor(a, b):

    bigger_num = a if a > b else b
    numbers = [int(num) for num in range(1, bigger_num + 1)]
    greatest = 1
    for number in numbers:
        if a % number == 0 and b % number == 0 and number > greatest:
            greatest = number
    return greatest


def solution(w, h):
    factor = greatest_common_factor(w, h)

    answer = w * h - factor * (w // factor + h // factor - 1)
    return answer


print(solution(8, 12))
print(solution(5, 5))
print(solution(2, 4))
