import sys


def find_fours(numbers, n, target):
    sums = {}
    cur_sum = 0
    for i in range(n):
        num = int(numbers[i])
        cur_sum += num
        print(f"curr_sum = {cur_sum}; index = {i}")


n = int(sys.stdin.readline())
s = int(sys.stdin.readline())
numbers = sys.stdin.readline().strip().split()
find_fours(numbers, n, s)
