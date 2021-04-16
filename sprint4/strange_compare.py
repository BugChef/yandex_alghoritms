import sys


def reveal(s, t):
    dic = {}
    dic_helper = {}
    result = True
    for i in range(len(s)):
        first = s[i]
        second = t[i]

        if first not in dic:
            if second in dic_helper:
                result = False
                break
            dic[first] = second
            dic_helper[second] = first

        if second != dic[first]:
            result = False
            break

    return result


s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

if len(s) == len(t):
    print('YES' if reveal(s, t) else 'NO')
else:
    print('NO')



