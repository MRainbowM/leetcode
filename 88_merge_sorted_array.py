# https://leetcode.com/problems/merge-sorted-array/description/

"""
88. Merge Sorted Array

Вам даны два целочисленных массива nums1и nums2,
отсортированных в неубывающем порядке,
и два целых числа m и n,
представляющие количество элементов в nums1 и nums2 соответственно.

Объединить nums1 и nums2 в один массив,
отсортированный в неубывающем порядке.

Окончательный отсортированный массив не должен возвращаться
функцией, а должен храниться внутри массива nums1.
Чтобы учесть это, nums1 имеет длину m + n,
где первые m элементы обозначают элементы,
которые должны быть объединены,
а последние n элементы установлены в 0 и должны игнорироваться.
nums2 имеет длину n.

# 1
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation:  Массивы, которые мы объединяем, — это [1,2,3] и [2,5,6].
Результатом слияния является [ 1,2,2,3,5,6 ]

# 2
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: Массивы, которые мы объединяем, — это [1] и [].
Результатом слияния является [1].


# 3
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: Массивы, которые мы объединяем, — это [] и [1].
Результат слияния — [1].
Обратите внимание, что поскольку m = 0,
в nums1 нет элементов.
0 присутствует только для того, чтобы гарантировать,
что результат слияния поместится в nums1.


Ограничения:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Продолжение: Можете ли вы придумать алгоритм,
работающий во O(m + n) времени?
"""
from typing import List


class Solution:
    def merge_v1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Runtime: 0 ms
        Memory: 17.98 МБ
        """
        if n == 0:
            return None

        if m == 0:
            for idx in range(0, n):
                nums1[idx] = nums2[idx]
            return None

        num2_save_idx = 0
        for idx in range(0, m + n):
            if num2_save_idx == n:
                return
            if (
                    nums2[num2_save_idx] <= nums1[idx] or
                    (idx >= m + num2_save_idx)
            ):
                nums1.insert(idx, nums2[num2_save_idx])
                num2_save_idx += 1
                nums1.pop(m + n)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Runtime: 0ms
        Memory: 17.99MB
        """

        m_idx = m - 1
        n_idx = n - 1
        cur_idx = m + n - 1

        while n_idx >= 0:
            if m_idx >= 0 and nums1[m_idx] > nums2[n_idx]:
                nums1[cur_idx] = nums1[m_idx]
                m_idx -= 1
            else:
                nums1[cur_idx] = nums2[n_idx]
                n_idx -= 1

            cur_idx -= 1


def tests():
    solution = Solution()

    nums1 = [-1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    solution.merge(
        nums1=nums1,
        m=5,
        nums2=[-1, -1, 0, 0, 1, 2],
        n=6
    )
    assert nums1 == [-1, -1, -1, 0, 0, 0, 0, 0, 1, 2, 3]

    nums1 = [1, 0]
    solution.merge(
        nums1=nums1,
        m=1,
        nums2=[2],
        n=1
    )
    assert nums1 == [1, 2]

    nums1 = [-1, 0, 0, 3, 3, 3, 0, 0, 0]
    solution.merge(
        nums1=nums1,
        m=6,
        nums2=[1, 2, 2],
        n=3
    )
    assert nums1 == [-1, 0, 0, 1, 2, 2, 3, 3, 3]

    nums1 = [2, 0]
    solution.merge(
        nums1=nums1,
        m=1,
        nums2=[1],
        n=1
    )
    assert nums1 == [1, 2]

    # 1
    nums1 = [1, 2, 3, 0, 0, 0]
    solution.merge(
        nums1=nums1,
        m=3,
        nums2=[2, 5, 6],
        n=3
    )

    assert nums1 == [1, 2, 2, 3, 5, 6]

    # 2
    nums1 = [1]
    solution.merge(
        nums1=nums1,
        m=1,
        nums2=[],
        n=0
    )

    assert nums1 == [1]

    # 3
    nums1 = [0]
    solution.merge(
        nums1=nums1,
        m=0,
        nums2=[1],
        n=1
    )

    assert nums1 == [1]


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
