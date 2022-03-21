def solution(land):
    def index_of(num):
        if num >= 0:
            return num
        else:
            return 4 + num

    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] = max(land[i - 1][index_of(j - 1)], land[i - 1][index_of(j - 2)], land[i - 1][index_of(j - 3)]) + land[i][j]
    return max(land[len(land) - 1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
