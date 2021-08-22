from collections import deque


def solution(gems):
    gem_count = len(set(gems))
    length = 100001
    gem_map = {}
    gem_queue = deque([])
    start = 0
    start_point = 0

    for gem in gems:
        if gem in gem_map:
            gem_map[gem] += 1
        else:
            gem_map[gem] = 1
        gem_queue.append(gem)
        while True:
            temp = gem_queue[0]
            if temp in gem_map and gem_map[temp] > 1:
                gem_map[temp] -= 1
                gem_queue.popleft()
                start_point += 1
            else:
                break

        if len(gem_map.keys()) == gem_count and length > len(gem_queue):
            length = len(gem_queue)
            start = start_point

    return [start + 1, start + length]


"""
["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]	
"""