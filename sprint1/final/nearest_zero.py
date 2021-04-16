"""
ID = 43752643
"""
import sys


# n - нужное кол-во чисел
# n = 0 -> []
# n = 2 -> [1, 1]
# n = 5 -> [1, 2, 3, 2, 1]
def get_numbers_between_zeroes(n):
    is_even = n % 2 == 0
    mid = n // 2 if is_even else n // 2 + 1
    if is_even:
        half = [i for i in range(1, mid + 1)]
        return half + half[::-1]
    else:
        half = [i for i in range(1, mid)]
        return half + [mid] + half[::-1]


# zero_index - индекс нуля
# zero_index = 0 -> []
# zero_index = 2 -> [2, 1]
def get_numbers_left_to_zero(zero_index):
    return [i for i in range(zero_index, 0, -1)]


# zero_index - индекс нуля
# end_index - конечный индекс
# zero_index = 1; end_index = 3 -> [1, 2]
# zero_index = 1; end_index = 1 -> []
def get_numbers_right_to_zero(zero_index, end_index):
    diff = end_index - zero_index
    return [i for i in range(1, diff + 1)]


"""
Номера домов нам не важны, нам важны только индексы
Первым делом я достаю все индексы пустых участков
А дальше задача сводится к тому, 
чтобы правильно расставить растояния между ними
Например вводим [1, 5, 0 , 8, 9, 12, 0, 15, 18]
1.Слева от первого нуля всегда будет убывающая до 1 последовательность  [2, 1]
2.Между нулей всегда будет 'массив палиндром' [1, 2, 1]
3.Справа от последнего нуля всегда будет возрастающая от 1 последовательность [1, 2]
"""


def main():
    street_length = int(sys.stdin.readline().strip())
    house_numbers = sys.stdin.readline().strip().split()

    # Ищем индексы пустых участков
    zero_indexes = [i for i in range(street_length) if house_numbers[i] == '0']

    # Итоговый массив с растояниями
    distance_to_zero = []

    # Итерируем по пустым участкам
    for i in range(len(zero_indexes)):
        zero_index = zero_indexes[i]

        # если на улице всего 1 пустой участок
        if len(zero_indexes) == 1:
            left_numbers = get_numbers_left_to_zero(zero_index)
            right_numbers = get_numbers_right_to_zero(zero_index, street_length - 1)
            distance_to_zero = left_numbers + [0] + right_numbers

        else:
            # случай, когда дома перед первым пустым участком
            if i == 0:
                left_numbers = get_numbers_left_to_zero(zero_index)
                distance_to_zero = left_numbers + [0]
            else:
                # случай, когда дома между пустых участков
                previous_zero_index = zero_indexes[i - 1]
                amount = zero_index - previous_zero_index - 1
                numbers_between_zeroes = get_numbers_between_zeroes(amount)
                distance_to_zero += numbers_between_zeroes
                distance_to_zero += [0]

                # если последний ноль в последовотельности
                if i == len(zero_indexes) - 1:
                    right_numbers = get_numbers_right_to_zero(zero_index, street_length - 1)
                    distance_to_zero += right_numbers

    print(' '.join(map(str, distance_to_zero)))


main()
