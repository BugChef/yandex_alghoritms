from itertools import product
from string import ascii_lowercase

a = 1000
m = 123987123


def hsh(string):
    lth = len(string)
    sm = ord(string[0]) if lth > 0 else 0
    for i in range(1, lth):
        sm = sm * a + ord(string[i])
    return sm % m


found_hashes = {}
for length in range(2, 1000):
    to_attempt = product(ascii_lowercase, repeat=length)
    for attempt in to_attempt:
        string = ''.join(attempt)
        h = hsh(string)
        if h not in found_hashes:
            found_hashes[h] = string
        else:
            print(found_hashes[h])
            print(string)