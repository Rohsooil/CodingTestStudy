def solution(numbers):
    def find_bit(number):
        if number % 2 == 0:
            return number + 1

        binary = format(number, "b")
        if "0" not in binary:
            binary = "10" + binary[1:]
            return int(binary, 2)

        last_zero = binary.rindex("0")
        if last_zero + 2 >= len(binary):
            binary = binary[:last_zero] + "10"
        else:
            binary = binary[:last_zero] + "10" + binary[last_zero + 2:]
        return int(binary, 2)

    answer = []

    for num in numbers:
        answer.append(find_bit(num))

    return answer


"""
101011011
10101101

"""

print(solution([343]))
# print(solution([2, 7, 5]))
# print(solution([1001, 337, 0, 1, 333, 673, 343, 221, 898, 997, 121, 1015, 665, 779, 891, 421, 222, 256, 512, 128, 100]))
"[1002, 338, 1, 2, 334, 674, 347, 222, 899, 998, 122, 1019, 666, 781, 893, 422, 223, 257, 513, 129, 101]"
