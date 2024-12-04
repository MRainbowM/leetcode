# https://leetcode.com/problems/add-two-numbers

"""
2. Add Two Numbers (Сложить два числа)

Задача:
Даны два непустых связанных списка, представляющих два неотрицательных целых числа.
Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру.
Сложите два числа и верните сумму в виде связанного списка.

Вы можете предположить, что эти два числа не содержат начальных нулей, за исключением самого числа 0.

# 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

# 2
Input: l1 = [0], l2 = [0]
Output: [0]

# 1
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Ограничения:
Количество узлов в каждом связанном списке находится в диапазоне [1, 100].
0 <= Node.val <= 9
Гарантируется, что список представляет собой число, не имеющее начальных нулей.
"""
from typing import List


# Определение односвязного списка
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        """Сравнение объектов"""
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

    def __ne__(self, other):
        return not self == other


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = current = ListNode(0)
        buff = 0

        # Цикл, пока в списках есть элементы или есть буфер для переноса
        while l1 or l2 or buff:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            cur_val = l1_val + l2_val + buff

            # Целое число от деления на 10 - перенос на след узел
            buff = cur_val // 10

            # В текущий узел остаток от деления
            current.next = ListNode(val=cur_val % 10)

            # Текущий узел - это next в родителе
            current = current.next

            # Переопределение списков
            # Текущий список - следующий узел
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


def genListNode(array: List[int]) -> ListNode:
    """
    Генерация связного списка
    """

    if len(array) == 1:
        return ListNode(val=array[0], next=None)

    head = ListNode(
        val=array[0],
        next=genListNode(array=array[1:])
    )

    return head


def tests():
    solution = Solution()

    result = solution.addTwoNumbers(
        l1=genListNode(array=[9, 9, 9, 9, 9, 9, 9]),
        l2=genListNode(array=[9, 9, 9, 9])
    )
    assert result == genListNode(array=[8, 9, 9, 9, 0, 0, 0, 1])

    result = solution.addTwoNumbers(
        l1=genListNode(array=[2, 4, 3]),
        l2=genListNode(array=[5, 6, 4])
    )
    assert result == genListNode(array=[7, 0, 8])

    result = solution.addTwoNumbers(
        l1=genListNode(array=[0]),
        l2=genListNode(array=[0])
    )
    assert result == genListNode(array=[0])

    result = solution.addTwoNumbers(
        l1=genListNode(array=[1]),
        l2=genListNode(array=[9])
    )
    assert result == genListNode(array=[0, 1])

    print("ВСЕ ЧИКИ-ПУКИ!!!")


if __name__ == "__main__":
    tests()
