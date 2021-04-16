"""
Метеорологическая служба вашего города решила измерять нестабильность погоды новым способом.
Назовём хаотичностью погоды за n дней число дней, в которые температура строго больше,
чем в день до (если такой существует) и в день после текущего (если такой существует).
Например, если за 5 дней температура воздуха составляла 1 2 5 4 8 градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись описанные условия.
Определите по ежедневным показаниям температуры хаотичность погоды за этот период.
"""

import sys

n = int(sys.stdin.readline())
if n > 1:
    line = sys.stdin.readline().strip()
    temperature_by_days = [int(x) for x in line.split()]

    chaotic_days_count = 0
    for i in range(n):
        if i == 0 and temperature_by_days[i] > temperature_by_days[i + 1]:
            chaotic_days_count += 1
        elif i == n - 1 and temperature_by_days[i] > temperature_by_days[i - 1]:
            chaotic_days_count += 1
        elif 0 < i < n - 1:
            current = temperature_by_days[i]
            previous = temperature_by_days[i - 1]
            next_day = temperature_by_days[i + 1]
            if current > previous and current > next_day:
                chaotic_days_count += 1

    print(chaotic_days_count)
else:
    print(1)
