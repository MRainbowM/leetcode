"""
Вычисление суммы элементов в массиве с помощью рекурсии
"""

from typing import List


def sum_list(number_list: List[int]) -> int:
    result = number_list[0]

    if len(number_list) == 1:
        return result
    else:
        result += sum_list(number_list=number_list[1:])

    return result


def tests():
    number_list = [1, 4, 6, 7, 9, 10]

    result = sum_list(number_list=number_list)

    assert result == 37

    print("OK")


tests()
