first = list(input())
second = list(input())

len_first = len(first)
len_second = len(second)

if abs(len_first - len_second) > 1:
    print("FAIL")
else:
    res = True
    itr = min(len_first, len_second)
    for i in range(itr):
        f = first[i]
        s = second[i]
        if f != s:
            if len_first == len_second:
                comp1 = first[i + 1:]
                comp2 = second[i + 1:]
                res = comp1 == comp2
            elif len_first > len_second:
                comp1 = first[i + 2:]
                comp2 = second[i + 1:]
                res = comp1 == comp2
            else:
                comp1 = first[i + 1:]
                comp2 = second[i + 2:]
                res = comp1 == comp2
            break
    print("OK" if res else "FAIL")
