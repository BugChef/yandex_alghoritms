#from node import Node

class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left

"""
        20
    19      21
  4   22
"""


def print_range(node: Node, l: int, r: int):
    if node is None:
        return

    if l < node.value:
        print_range(node.left, l, r)

    if l <= node.value <= r:
        print(node.value)

    if r > node.value:
        print_range(node.right, l, r)


k1 = 10
k2 = 25
root = Node(value=20)
root.left = Node(value=19)
root.right = Node(value=21)
root.left.left = Node(value=4)
root.left.right = Node(value=22)

print_range(root, k1, k2)