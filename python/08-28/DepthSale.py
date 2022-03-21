def solution(enroll, referral, seller, amount):
    person_map = {"center": {"earned": 0, "parent": None}}

    for i in range(len(enroll)):
        person_map[enroll[i]] = {"earned": 0}
        if referral[i] != '-':
            person_map[enroll[i]]["parent"] = referral[i]
        else:
            person_map[enroll[i]]["parent"] = "center"

    for i in range(len(seller)):
        sell_people = seller[i]
        earned_amount = amount[i] * 100

        temp = sell_people

        while temp is not None:
            money = earned_amount - earned_amount // 10
            person_map[temp]["earned"] += money
            temp = person_map[temp]["parent"]
            earned_amount = earned_amount // 10
            if earned_amount == 0:
                break

    answer = []

    for person in enroll:
        answer.append(person_map[person]["earned"])

    return answer
