def sift_up(heap: list, idx: int) -> int:
    if idx == 1:
        return 1

    parent_index = idx // 2

    if heap[parent_index] < heap[idx]:
        heap[parent_index], heap[idx] = heap[idx], heap[parent_index]
        return sift_up(heap, parent_index)
    else:
        return idx
