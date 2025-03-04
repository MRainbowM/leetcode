# https://leetcode.com/problems/intersection-of-two-arrays/description/

"""
349. Intersection of Two Arrays

Даны два целочисленных массива nums1и nums2,
вернуть массив их пересечение.
Каждый элемент в результате должен быть уникальным,
и вы можете вернуть результат в любом порядке.

# 1
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

# 2
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] также принимается.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List


class Solution:
    def intersection_v1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 7ms
        Memory: 17.70MB
        """
        result = set([i for i in nums1 if i in nums2])
        return list(result)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 0ms
        Memory: 17.93MB
        """

        result = list(set(nums1).intersection(set(nums2)))
        return result

    def intersection_v3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Runtime: 44ms
        Memory: 18.14MB
        """
        nums1.sort()
        nums2.sort()

        m = len(nums1)
        n = len(nums2)

        m_idx = 0
        n_idx = 0

        result = []

        while m_idx < m and n_idx < n:
            if nums1[m_idx] == nums2[n_idx]:
                result.append(nums1[m_idx])
                m_idx += 1
                n_idx += 1
            elif nums1[m_idx] > nums2[n_idx]:
                n_idx += 1
            else:
                m_idx += 1

        return list(set(result))


def tests():
    solution = Solution()

    # 1
    result = solution.intersection(
        nums1=[1, 2, 2, 1],
        nums2=[2, 2]
    )

    assert result == [2]

    # 2
    result = solution.intersection(
        nums1=[4, 9, 5],
        nums2=[9, 4, 9, 8, 4]
    )
    assert {4, 9} == set(result)


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
