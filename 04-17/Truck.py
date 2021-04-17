from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_queue = deque(truck_weights)
    answer = 0
    total_weight = 0

    while truck_queue:
        answer += 1
        out_truck = bridge.popleft()
        total_weight -= out_truck
        next_truck = truck_queue[0]
        if (total_weight + next_truck) > weight:
            bridge.append(0)
        else:
            total_weight += next_truck
            bridge.append(truck_queue.popleft())

    answer += bridge_length
    return answer
