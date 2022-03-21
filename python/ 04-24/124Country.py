def solution(n):
    def recurse(num):

        if num == 0:
            return '1'
        elif num == 1:
            return '2'
        elif num == 2:
            return '4'
        else:
            return recurse((num // 3) - 1) + recurse(num % 3)

    # 여기는 배열로 풀어본 부분입니다.
    # memo = ['1', '2', '4']
    # for i in range(3, n):
    #     memo.append(memo[(i // 3) - 1] + memo[i % 3])

    answer = recurse(n - 1)
    return answer


for i in range(1, 20):
    print(solution(i))
