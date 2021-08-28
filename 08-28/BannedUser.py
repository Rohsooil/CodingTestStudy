import re


def solution(user_id, banned_id):
    banned_set_list = []
    visited = [False for _ in range(len(user_id))]

    def dfs(depth, stack):
        if depth >= len(banned_id):
            if set(stack) not in banned_set_list:
                banned_set_list.append(set(stack))
            return
        pattern = re.compile(banned_id[depth].replace("*", ".?"))

        for idx, user in enumerate(user_id):
            if visited[idx]:
                continue

            if len(banned_id[depth]) != len(user):
                continue
            searched = pattern.search(user)
            if searched and user == searched.group():
                visited[idx] = True
                stack.append(user)
                dfs(depth + 1, stack)
                stack.pop()
                visited[idx] = False

    dfs(0, [])
    return len(banned_set_list)
