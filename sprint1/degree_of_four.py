"""
Вася на уроке математики проходил степени.
Он хочет написать программу, которая определяет,
будет ли положительное целое число степенью четверки.
"""
import sys
import math

number = int(sys.stdin.readline().strip())
log = math.log(number, 4)
isDegree = log.is_integer()
print(isDegree)