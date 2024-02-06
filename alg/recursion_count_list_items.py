"""
Подсчет количества элементов в списке с помощью рекурсии
"""

from typing import List


def count_list_items(number_list: List[int]) -> int:
    if number_list == list():
        return 0
    else:
        return 1 + count_list_items(number_list[1:])


def tests():
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    result = count_list_items(number_list=number_list)

    assert result == 9

    print("OK")


tests()
