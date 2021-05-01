from itertools import permutations


def solution(numbers):
    number_list = [int(num) for num in numbers]
    number_list.sort(reverse=True)
    # 숫자 역순 정렬 후 합쳐서 최대값을 구함
    max_number = int(''.join([str(num) for num in number_list]))

    # 최대값 까지의 소수 판별을 위한 배열 선언
    prime_list = [True for _ in range(max_number + 1)]
    # 0, 1 은 소수가 아니므로 False
    prime_list[0], prime_list[1] = False, False

    for i in range(2, max_number + 1):
        if prime_list[i] is True:
            # 제곱수 부터 자기자신을 곱한값은 전부 소수가 아니므로 False
            for j in range(i * i, max_number + 1, i):
                prime_list[j] = False

    answer = 0
    permute_list = []

    for i in range(1, len(number_list) + 1):
        # 뽑는 순서가 있으므로 순열을 이용해서 리스트를 만듬
        temp_permute = permutations(number_list, i)
        for temp_number in temp_permute:
            permute_list.append(int("".join([str(s) for s in temp_number])))

    # 순열 리스트 중복 제거
    permute_list = list(set(permute_list))

    # 순열 리스트 중에 소수를 찾고 answer + 1
    for num in permute_list:
        if prime_list[num] is True:
            answer += 1

    return answer


print(solution('17'))
print(solution('011'))
