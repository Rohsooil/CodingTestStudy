from collections import deque


def solution(n, t, m, timetable):
    start = "09:00"
    bus_map = {start: {"crew": 0, "last": None}}
    timetable.sort()
    queue = deque(timetable)

    def add_time(at, amount):
        hour, minute = at.split(":")
        result = int(hour) * 60 + int(minute) + amount
        return '%02d:%02d' % (result // 60, result % 60)

    now = start

    for i in range(1, n):
        next_bus = add_time(start, i * t)
        bus_map[next_bus] = {"crew": 0, "last": None}

    while queue:
        if n <= 0:
            break
        next_man = queue[0]
        if next_man <= now and bus_map[now]["crew"] < m:
            bus_map[now]["crew"] += 1
            bus_map[now]["last"] = next_man
            queue.popleft()
        else:
            now = add_time(now, t)
            n -= 1

    now = sorted(bus_map.keys())[-1]
    if bus_map[now]["last"] and bus_map[now]["crew"] == m:
        now = add_time(bus_map[now]["last"], -1)

    return now
