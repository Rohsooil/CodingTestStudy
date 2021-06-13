def solution(citations):
    citations.sort()
    answer = 0

    def count_exceed(numbers, target):
        count = 0
        for number in numbers:
            if number >= target:
                count += 1
        return count

    def count_leak(numbers, target):
        count = 0
        for number in numbers:
            if number <= target:
                count += 1
        return count

    for i in range(len(citations)):
        temp_h_index = len(citations) - i
        if count_exceed(citations, temp_h_index) >= temp_h_index >= count_leak(citations, temp_h_index):
            answer = temp_h_index
            break
    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([994, 997, 996, 1, 995]))
