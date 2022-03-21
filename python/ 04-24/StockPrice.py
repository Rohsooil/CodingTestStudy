def solution(prices):
    answer = []

    for i in range(len(prices)):
        price = prices[i]
        answer.append(0)
        for j in range(i + 1, len(prices)):
            answer[i] += 1
            if prices[j] < price:
                break

    return answer


print(solution([1, 2, 3, 2, 3]))
