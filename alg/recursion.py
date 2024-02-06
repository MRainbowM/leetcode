"""
Вычисление суммы элементов в массиве с помощью рекурсии
"""

from typing import List


def sum_list_v2(number_list: List[int]) -> int:
    if len(number_list) == 0:
        return 0
    else:
        return number_list[0] + sum_list_v2(number_list=number_list[1:])


def sum_list_v1(number_list: List[int]) -> int:
    result = number_list[0]

    if len(number_list) == 1:
        return result
    else:
        result += sum_list_v1(number_list=number_list[1:])

    return result


def tests():
    number_list = [1, 4, 6, 7, 9, 10]

    result = sum_list_v1(number_list=number_list)

    assert result == 37

    result = sum_list_v2(number_list=number_list)

    assert result == 37

    print("OK")


tests()
