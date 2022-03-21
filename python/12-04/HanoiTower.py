def solution(n):
    answer = []

    def path(start, goal):
        answer.append([start, goal])

    def hanoi(number, start, goal, middle):
        if number == 1:
            path(start, goal)
        else:
            hanoi(number - 1, start, middle, goal)
            path(start, goal)
            hanoi(number - 1, middle, goal, start)

    hanoi(n, 1, 3, 2)
    return answer
