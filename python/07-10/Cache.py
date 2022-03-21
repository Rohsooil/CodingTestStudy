def solution(cache_size, cities):
    cache = {}
    cache_hit = 1
    cache_miss = 5
    recently_used = 0

    answer = 0
    for city in cities:
        key = city.lower()

        if key in cache:
            answer += cache_hit
            cache[key] = recently_used
        else:
            answer += cache_miss
            cache[key] = recently_used
            if len(cache.keys()) > cache_size:
                used_earliest = min(cache, key=cache.get)
                del cache[used_earliest]
        recently_used += 1

    return answer


"""
{
    "NewYork" : 3,
    "LA" : 4,
    "Jeju" : 5
}
"""

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
