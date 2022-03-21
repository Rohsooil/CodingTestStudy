from datetime import datetime, timedelta

TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"


def solution(lines):
    time_list = []

    def line_to_time(date, seconds):
        end = datetime.strptime(date, TIME_FORMAT)
        start = end - timedelta(seconds=(seconds - 0.001))
        return start, end

    for line in lines:
        split = line.split()
        start_time, end_time = line_to_time(' '.join([split[0], split[1]]), float(split[2].replace('s', '')))
        time_list.append((start_time, end_time))

    answer = 0
    for i in range(len(time_list)):
        count = 0
        comparison_time = time_list[i][1]
        for j in range(i, len(time_list)):
            if comparison_time > time_list[j][0] - timedelta(seconds=1):
                count += 1
        answer = max(answer, count)
    return answer


"""
 
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"

"""