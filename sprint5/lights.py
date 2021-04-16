class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(node) -> int:
    if node is None:
        return 0
    res = node.value
    left = solution(node.left)
    right = solution(node.right)
    if left > res:
        res = left
    if right > res:
        res = right
    return res