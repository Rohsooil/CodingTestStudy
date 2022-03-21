def solution(fees, records):
    base_minutes, base_fee, unit_minutes, unit_fee = fees
    car_map = {}

    def time_gap(time1, time2):
        hour1, minute1 = time1.split(":")
        hour2, minute2 = time2.split(":")

        sum_of_minute1 = int(hour1) * 60 + int(minute1)
        sum_of_minute2 = int(hour2) * 60 + int(minute2)

        return sum_of_minute2 - sum_of_minute1

    def calculate_minutes(minute1, minute2):
        if minute1 - minute2 < 0:
            return 0
        if (minute1 - minute2) % unit_minutes > 0:
            return ((minute1 - minute2) // unit_minutes) * unit_minutes + unit_minutes
        return minute1 - minute2

    for record in records:
        time, car_number, action = record.split(" ")
        if car_number not in car_map:
            car_map[car_number] = {"IN": time, "accumulated": 0}
        else:
            if action == "IN":
                car_map[car_number]["IN"] = time
            else:
                in_time = car_map[car_number]["IN"]
                car_map[car_number]["IN"] = None
                car_map[car_number]["accumulated"] += time_gap(in_time, time)

    for key in car_map.keys():
        if car_map[key]["IN"] is not None:
            in_time = car_map[key]["IN"]
            car_map[key]["IN"] = None
            car_map[key]["accumulated"] += time_gap(in_time, "23:59")

    answer = []

    car_keys = sorted(car_map.keys())

    for key in car_keys:
        total_fee = base_fee + (calculate_minutes(car_map[key]["accumulated"], base_minutes)) // unit_minutes * unit_fee
        answer.append(total_fee)
    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
