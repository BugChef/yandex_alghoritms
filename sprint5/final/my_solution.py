"""
ID = 48712296

Сложность написана в условии)) O(h)
Дополнительная память не используется O(1)
"""


class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def min_value(node: Node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def remove(root: Node, key: int) -> Node:
    if root is None:
        return root

    if key < root.value:
        root.left = remove(root.left, key)
    elif key > root.value:
        root.right = remove(root.right, key)
    else:
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        temp = min_value(root.right)
        root.value = temp.value
        root.right = remove(root.right, temp.value)

    return root
