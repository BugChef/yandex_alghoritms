import sys

def max_length(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        el = int(arr[i])

        if el == 0:
            curr_sum -= 1
        else:
            curr_sum += 1

        if curr_sum is 0:
            max_len = i + 1

        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i

    return max_len


n = int(sys.stdin.readline())
results = sys.stdin.readline().strip().split()
print(max_length(results))