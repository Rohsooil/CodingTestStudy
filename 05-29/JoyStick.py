def solution(name):
    up_down_list = []
    A_CODE, N_CODE, Z_CODE = 65, 78, 90
    for i in range(len(name)):
        ascii_code = int(ord(name[i]))
        if ascii_code < N_CODE:
            up_down_list.append(ascii_code - A_CODE)
        else:
            up_down_list.append(abs(ascii_code - (Z_CODE + 1)))

    idx, answer = 0, 0

    # 좌 또는 우로 이동해야할 경우 최솟값을 구함
    while True:
        answer += up_down_list[idx]
        up_down_list[idx] = 0
        if sum(up_down_list) == 0:
            break
        left, right = 1, 1
        while up_down_list[idx - left] == 0:
            left += 1
        while up_down_list[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    return answer


print(solution("JEROEN"))
print(solution("JAN"))
print(solution("ABC"))
print(solution("AAZAAA"))
print(solution("AZAAAZ"))
