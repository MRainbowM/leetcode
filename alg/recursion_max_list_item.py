"""
Нахождение наибольшего числа в списке с помощью рекукрсии
"""

from typing import List, Optional


def max_list_item_v1(number_list: List[int]) -> Optional[int]:
    if number_list == list():
        return

    if len(number_list) == 1:
        return number_list[0]

    number_list.pop(1) if number_list[0] >= number_list[1] else number_list.pop(0)

    return max_list_item_v1(number_list=number_list)


def tests():
    number_list = [1, 4, 6, 21, 7, 9, 10]

    result = max_list_item_v1(number_list=number_list)

    assert result == 21

    number_list = [100]

    result = max_list_item_v1(number_list=number_list)

    assert result == 100

    print("OK")


tests()
