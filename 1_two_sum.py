# https://leetcode.com/problems/two-sum
"""
1. Two Sum

Дан массив целых чисел nums и целое число target,
вернуть индексы двух чисел, чтобы их сумма давала target.

Вы можете предположить, что каждый вход будет иметь ровно одно решение,
и вы не можете использовать один и тот же элемент дважды.

Вы можете возвращать ответ в любом порядке.

# 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 2
Input: nums = [3,2,4], target = 6
Output: [1,2]

# 3
Input: nums = [3,3], target = 6
Output: [0,1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue

                if nums[i] + nums[j] == target:
                    return [i, j]


def tests():
    solution = Solution()

    result = solution.twoSum(
        nums=[2, 7, 11, 15],
        target=9
    )
    assert set(result) == {0, 1}

    result = solution.twoSum(
        nums=[3, 2, 4],
        target=6
    )
    assert set(result) == {1, 2}

    result = solution.twoSum(
        nums=[3, 3],
        target=6
    )
    assert set(result) == {0, 1}


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
