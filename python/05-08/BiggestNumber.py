def solution(numbers):
    # string 으로 만들어서 자리수 만큼 곱하고 내림차순 정렬
    number_list = [(index, str(num) * 3) for (index, num) in enumerate(numbers)]
    number_list.sort(key=lambda x: x[1], reverse=True)
    answer = ''
    for element in number_list:
        answer += str(numbers[element[0]])

    return str(int(answer))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0, 10, 1000]))
