def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    answer = 1

    for key in clothes_dict:
        answer *= (clothes_dict[key] + 1)

    answer -= 1
    return answer
