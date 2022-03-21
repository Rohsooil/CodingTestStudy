def solution(n, words):
    word_dict = {}

    answer = []
    for idx, word in enumerate(words):
        if idx > 0:
            if words[idx - 1][-1] != words[idx][0]:
                answer.append(idx % n + 1)
                answer.append(idx // n + 1)
                break
        if word in word_dict:
            answer.append(idx % n + 1)
            answer.append(idx // n + 1)
            break
        word_dict[word] = 0

    if not answer:
        answer.append(0)
        answer.append(0)

    return answer


print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference",
                   "estimate", "executive"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
