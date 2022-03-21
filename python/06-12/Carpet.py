def solution(brown, yellow):
    division_numbers = []

    for i in range(1, int(yellow ** (1 / 2)) + 1):
        if yellow % i == 0:
            division_numbers.append((i, yellow // i))

    answer = []
    for division in division_numbers:
        square_width = (division[0] + 2) * (division[1] + 2)
        yellow_width = division[0] * division[1]

        if brown == square_width - yellow_width:
            answer.extend([division[1] + 2, division[0] + 2])
            break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
