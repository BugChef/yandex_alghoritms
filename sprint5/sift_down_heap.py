class Node:
    def __init__(self, left=None, right=None, value=0):
        self.value = value
        self.right = right
        self.left = left


def sift_down(heap, idx) -> int:
    left = 2 * idx
    right = 2 * idx + 1

    if len(heap) - 1 < left:
        return idx

    if right <= len(heap) - 1 and heap[left] < heap[right]:
        index_largest = right
    else:
        index_largest = left

    if heap[idx] < heap[index_largest]:
        heap[idx], heap[index_largest] = heap[index_largest], heap[idx]
        return sift_down(heap, index_largest)
    else:
        return idx
