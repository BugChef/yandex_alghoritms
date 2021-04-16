class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def insert(root: Node, key: int) -> Node:
    if root is None:
        return Node(value=key)

    if key < root.value:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root

