import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

current_max = -1
current_block = []
blocks = []
for i in range(n - 1):
    number = numbers[i]
    next_number = numbers[i + 1]

    current_block.append(number)

    if current_max < 0:
        current_max = number

    if next_number > current_max:
        current_max = -1
        blocks.append(current_block)
        current_block = []

    if i == n - 2:
        if next_number > current_max and len(current_block) != 0:
            blocks.append(current_block)
            blocks.append([next_number])
        else:
            current_block.append(next_number)
            blocks.append(current_block)

i = len(blocks) - 1
while i != 0:
    current_block = blocks[i]
    prev_block = blocks[i - 1]

    current_block.sort()
    prev_block.sort()

    current_block_min = current_block[0]
    prev_block_max = prev_block[-1]

    if current_block_min < prev_block_max:
        new_block = current_block + prev_block
        blocks.pop(i)
        blocks.pop(i - 1)
        blocks.insert(i, new_block)
    i -= 1

print(len(blocks))



