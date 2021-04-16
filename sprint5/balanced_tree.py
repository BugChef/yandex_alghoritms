class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def solution(root: Node) -> bool:
    return is_balanced_helper(root) > -1


def is_balanced_helper(root: Node):
    if root is None:
        return 0

    left_height = is_balanced_helper(root.left)
    if left_height == -1:
        return -1

    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1