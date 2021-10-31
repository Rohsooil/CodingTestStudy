def solution(stones, k):
    left, right = 1, max(stones)
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        blank = 0
        flag = True
        for stone in stones:
            if stone < mid:
                blank += 1
                if blank == k:
                    flag = False
                    break
            else:
                blank = 0
        if flag:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1
    return answer
