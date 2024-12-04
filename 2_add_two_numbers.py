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
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        """Сравнение объектов"""
        if isinstance(other, Node):
            return self.val == other.val and self.next == other.next
        return False

    def __ne__(self, other):
        return not self == other


class Solution:

    def addTwoNumbers(
            self,
            l1: List[Node],
            l2: List[Node]
    ) -> List[Node]:
        """"""
        out = []
        buff, idx = 0, 0
        last_idx = max(len(l1), len(l2))
        cur_next = None
        while True:

            if cur_next is None:
                # Первый элемент
                cur_val = (
                        (l1[idx].val if len(l1) > idx else 0) +
                        (l2[idx].val if len(l2) > idx else 0)
                )
                if cur_val >= 10:
                    buff = 1
                    cur_val = cur_val - 10
            else:
                cur_val = cur_next

            if idx == last_idx - 1:
                if buff == 1:
                    out.append(Node(val=cur_val, next=1))
                    out.append(Node(val=1, next=None))
                else:
                    out.append(Node(val=cur_val, next=None))
                break

            cur_next = (
                    (l1[idx].next if len(l1) > idx and l1[idx].next else 0) +
                    (l2[idx].next if len(l2) > idx and l2[idx].next else 0) +
                    buff
            )
            buff = 0

            if cur_next >= 10:
                buff = 1
                cur_next = cur_next - 10

            out.append(Node(val=cur_val, next=cur_next))

            idx += 1

        return out


def genListNode(array: List[int]) -> List[Node]:
    """
    Генерация связного списка

    :param array: List[int] - список чисел
    :return: List[ListNode] - связный список
    """
    len_array = len(array)

    # out = []
    # for idx in range(len_array):
    #     out.append(
    #         ListNode(
    #             val=array[idx],
    #             next=array[idx + 1] if idx + 1 < len_array else None
    #         )
    #     )

    out = [Node(
        val=array[idx],
        next=array[idx + 1] if idx + 1 < len_array else None
    ) for idx in range(len_array)]

    return out


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
