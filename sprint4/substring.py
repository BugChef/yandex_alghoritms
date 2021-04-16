
def longest_substtr(s):
    last_index = [-1] * 256

    n = len(s)
    res = 0
    i = 0

    for j in range(0, n):
        i = max(i, last_index[ord(s[j])] + 1)
        res = max(res, j - i + 1)
        last_index[ord(s[j])] = j

    return res


string = input()
print(longest_substtr(string))