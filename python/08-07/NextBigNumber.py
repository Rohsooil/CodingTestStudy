def solution(n):
    to_str = "{0:b}".format(n)
    number_of_one = to_str.count('1')
    next_number = n + 1
    while True:
        next_str = "{0:b}".format(next_number)
        next_of_one = next_str.count('1')
        if number_of_one == next_of_one:
            answer = next_number
            break
        next_number += 1

    return answer


print(solution(78))
print(solution(15))
