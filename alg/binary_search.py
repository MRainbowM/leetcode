"""Бинарный поиск"""

from typing import List, Optional


def binary_search(number_list: List[int], search_el: int) -> Optional[int]:
    low = 0
    high = len(number_list) - 1

    while low <= high:
        # Поиск середины
        mid = int((low + high) / 2)
        # Значение среднего элемента
        mid_el = number_list[mid]

        if mid_el == search_el:
            # Элемент найден
            return mid
        if mid_el > search_el:
            # Искомое значение меньше
            high = mid - 1
        else:
            # Искомое значение больше
            low = mid + 1

    return None


def tests():
    number_list = [2, 4, 5, 7, 9, 10, 20, 23]

    position = binary_search(number_list=number_list, search_el=9)
    assert position == 4

    position = binary_search(number_list=number_list, search_el=-1)
    assert position is None

    print("OK")


tests()
