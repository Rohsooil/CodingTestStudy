import re


def solution(record):

    enter_pattern = r'Enter (.*) (.*)'
    leave_pattern = r'Leave (.*)'
    change_pattern = r'Change (.*) (.*)'

    id_nickname = {}

    answer = []

    for chat in record:
        if "Enter" in chat:
            match = re.match(enter_pattern, chat)
            id_nickname[match.group(1)] = match.group(2)
            answer.append(f"{match.group(1)}님이 들어왔습니다.")
        elif "Leave" in chat:
            match = re.match(leave_pattern, chat)
            answer.append(f"{match.group(1)}님이 나갔습니다.")
        elif "Change" in chat:
            match = re.match(change_pattern, chat)
            id_nickname[match.group(1)] = match.group(2)

    for i in range(len(answer)):
        if "들어왔습니다." in answer[i]:
            usr_id = re.match(r"(.*)님이 들어왔습니다.", answer[i]).group(1)
            answer[i] = re.sub(usr_id, id_nickname[usr_id], answer[i])
        elif "나갔습니다." in answer[i]:
            usr_id = re.match(r"(.*)님이 나갔습니다.", answer[i]).group(1)
            answer[i] = re.sub(usr_id, id_nickname[usr_id], answer[i])

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))
