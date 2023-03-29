# https://leetcode.com/problems/house-robber/

# runtime:	27 ms
# memory: 13.8 MB
# сложность по вычислениям: O(n), n - кол-во элементов в массиве
# сложность по памяти: O(1)

"""
198. House Robber

Задача:
Вы профессиональный грабитель, планирующий ограбить дома вдоль улицы.
В каждом доме спрятана определенная сумма денег.
Единственное ограничение, мешающее вам ограбить каждый из них, заключается в том,
что в соседних домах подключена система безопасности,
и она автоматически свяжется с полицией, если два соседних дома будут взломаны в одну и ту же ночь.

Учитывая целочисленный массив nums, представляющий сумму денег в каждом доме,
верните максимальную сумму денег, которую вы можете награбить сегодня вечером,
не привлекая внимания полиции.

# 1
Input: nums = [1,2,3,1]
Output: 4
Explanation: Ограбить дом 1 (деньги = 1), а затем ограбить дом 3 (деньги = 3).
Общая сумма = 1 + 3 = 4.

# 2
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Ограбить дом 1 (деньги = 2), ограбить дом 3 (деньги = 9) и ограбить дом 5 (деньги = 1).
Общая сумма = 2 + 9 + 1 = 12.
"""
from typing import List


class Solution:
    """A class with a solution to problem 198."""

    def rob(self, nums: List[int]) -> int:
        """
        The rob function takes in a list of house values and returns the maximum amount of money
        you can rob without alerting the police.

        :param self: Reference the object that is calling the method
        :param nums:List[int]: Represent the list of houses that need to be robbed
        :return: The maximum amount of money you can rob tonight without alerting the police
        :doc-author: Trelent
        """
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # if len(nums) == 2:
        #     max(nums[0], nums[1])

        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])

        return max(nums[-1], nums[-2])


def tests():
    """
    The tests function runs a series of tests to check that the behavior of
    the `rob` function is as expected.

    :doc-author: Trelent
    """

    solution = Solution()

    result = solution.rob(nums=[2, 7, 9, 3, 1])
    assert result == 12

    result = solution.rob(nums=None)
    assert result == 0

    result = solution.rob(nums=[])
    assert result == 0

    result = solution.rob(nums=[7, 2, 9, 3, 1])
    assert result == 17

    result = solution.rob(nums=[1, 2, 3, 1])
    assert result == 1 + 3

    result = solution.rob(nums=[1, 2])
    assert result == 2

    result = solution.rob(nums=[5])
    assert result == 5

    result = solution.rob(nums=[2, 1, 1, 2])
    assert result == 4

    print("OK")


tests()
