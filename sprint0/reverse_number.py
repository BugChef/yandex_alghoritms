n = int(input())

if n % 10 == 0:
    n = int(n / 10)

reversed_number = 0
abs_n = abs(n)

while abs_n != 0:
    digit = abs_n % 10
    reversed_number = reversed_number * 10 + digit
    abs_n = abs_n // 10

print(reversed_number if n > 0 else reversed_number * -1)