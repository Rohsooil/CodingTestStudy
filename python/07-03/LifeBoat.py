def solution(people, limit):
    answer = 0
    people.sort()

    left, right = 0, len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            people[left], people[right] = 0, 0
            left += 1
            right -= 1
            answer += 1
            continue
        right -= 1

    for person in people:
        if person != 0:
            answer += 1

    return answer


print(solution([80, 80, 50, 30, 20, 20], 100))
print(solution([70, 50, 80, 50], 100))
print(solution([70, 50, 80], 100))
