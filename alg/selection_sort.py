"""
Сортировка выбором
O(n^2)
"""

from typing import List


def _find_min(number_list: List[int]) -> int:
    """Поиск индекса минимального элемента в списке"""
    min_el = number_list[0]
    min_index = 0

    for i in range(0, len(number_list)):
        if number_list[i] < min_el:
            min_el = number_list[i]
            min_index = i

    return min_index


def selection_sort(number_list: List[int]) -> List[int]:
    new_list = []

    for i in range(0, len(number_list)):
        min_index = _find_min(number_list=number_list)

        # Удаление элемента из исходного списка
        el = number_list.pop(min_index)

        new_list.append(el)

    return new_list


def test():
    number_list = [3, 10, 15, 5, 2, 7, 9]

    sort_list = selection_sort(number_list=number_list)

    assert sort_list == [2, 3, 5, 7, 9, 10, 15]

    print("OK")


test()
