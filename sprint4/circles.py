n = int(input())
circle_names = set()
for _ in range(n):
    circle_name = input()
    if circle_name not in circle_names:
        print(circle_name)
        circle_names.add(circle_name)