from collections import deque


def solution(priorities, location):
    answer = 0
    print_queue = deque([(value, idx) for idx, value in enumerate(priorities)])

    while True:
        next_print = print_queue.popleft()
        if print_queue and max(print_queue)[0] > next_print[0]:
            print_queue.append(next_print)
        else:
            answer += 1
            if next_print[1] == location:
                break

    return answer
