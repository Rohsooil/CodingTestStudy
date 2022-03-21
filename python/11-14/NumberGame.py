def solution(A, B):
    A.sort()
    B.sort()

    start = 0
    answer = 0

    for i in range(len(A)):
        for j in range(start, len(B)):
            if A[i] < B[j]:
                answer += 1
                start = j + 1
                break

    return answer
