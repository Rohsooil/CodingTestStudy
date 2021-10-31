import sys

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    for idx, node in enumerate(nodeinfo):
        nodeinfo[idx].append(idx + 1)

    nodeinfo.sort(key=lambda x: (x[1]), reverse=True)
    tree = {}
    for idx, node in enumerate(nodeinfo):
        new_tree = {"x": node[0], "y": node[1], "index": node[2], "right": None, "left": None}
        if idx == 0:
            tree = new_tree
        else:
            current = tree
            while True:
                if current["x"] < new_tree["x"]:
                    if current["right"] is None:
                        current["right"] = new_tree
                        break
                    else:
                        current = current["right"]
                else:
                    if current["left"] is None:
                        current["left"] = new_tree
                        break
                    else:
                        current = current["left"]

    def pre_order(element, arr):
        if element is None:
            return arr
        arr.append(element["index"])
        pre_order(element["left"], arr)
        pre_order(element["right"], arr)
        return arr

    def post_order(element, arr):
        if element is None:
            return arr
        post_order(element["left"], arr)
        post_order(element["right"], arr)
        arr.append(element["index"])
        return arr

    answer = [pre_order(tree, []), post_order(tree, [])]
    return answer
