import math


def solution(n, k):
    def is_prime_num(number):
        if number == 1 or number == 0:
            return False

        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False

        return True

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

    def convert_base_k(number):
        base_k = ''
        while number // k != 0:
            remain = number % k
            base_k = get_remain(remain) + base_k
            number = number // k
        base_k = get_remain(number) + base_k
        return base_k

    converted = convert_base_k(n)
    if '0' not in converted and is_prime_num(int(converted)):
        return 1

    answer = 0

    temp_str = ""
    for idx, s in enumerate(converted):
        if not temp_str and s == '0':
            continue
        if s == '0':
            if is_prime_num(int(temp_str)):
                answer += 1
            temp_str = ""
            continue
        temp_str += s
    if temp_str and is_prime_num(int(temp_str)):
        answer += 1

    return answer


print(solution(437674, 3))
print(solution(110011, 10))
print(solution(999999, 9))
