# https://leetcode.com/problems/max-consecutive-ones/description
"""
485. Max Consecutive Ones

Для заданного двоичного массива nums
вернуть максимальное количество последовательных 1-элементов в массиве.


# 1
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: Первые две цифры или последние три цифры — последовательные 1.
Максимальное количество последовательных 1 — 3.

# 2
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Runtime: 8ms
        Memory: 20.24MB
        """
        max_consecutive_ones = 0
        temp = 0

        for i in nums:
            if i == 1:
                temp += 1
            else:
                if temp > max_consecutive_ones:
                    max_consecutive_ones = temp
                temp = 0

        return max(temp, max_consecutive_ones)


def tests():
    solution = Solution()

    # 1
    result = solution.findMaxConsecutiveOnes(
        nums=[1, 1, 0, 1, 1, 1]
    )
    assert result == 3

    # 2
    result = solution.findMaxConsecutiveOnes(
        nums=[1, 0, 1, 1, 0, 1]
    )
    assert result == 2


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
