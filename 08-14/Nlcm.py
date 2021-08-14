def solution(arr):
    def gcd(first, second):
        if second == 0:
            return first
        return gcd(second, first % second)

    def lcm(first, second):
        return first * second // gcd(first, second)

    arr.sort(reverse=True)
    answer = arr[0]

    for i in range(1, len(arr) - 1):
        if answer % arr[i] == 0:
            continue
        else:
            answer = lcm(answer, arr[i])

    return answer
