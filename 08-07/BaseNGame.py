def solution(n, t, m, p):
    answer = ''

    def get_remain(number):
        if number >= 10:
            if number - 10 == 0:
                return 'A'
            elif number - 10 == 1:
                return 'B'
            elif number - 10 == 2:
                return 'C'
            elif number - 10 == 3:
                return 'D'
            elif number - 10 == 4:
                return 'E'
            elif number - 10 == 5:
                return 'F'
        else:
            return str(number)

    def convert_base_n(number):
        base_n = ''
        while number // n != 0:
            remain = number % n
            base_n = get_remain(remain) + base_n
            number = number // n
        base_n = get_remain(number) + base_n
        return base_n

    collected_number = '0'

    for i in range(1, t * m + 1):
        collected_number += convert_base_n(i)

    current = p - 1
    while len(answer) < t:
        answer += collected_number[current]
        current += m
    return answer


print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))
# print(solution(16, 16, 2, 2))
