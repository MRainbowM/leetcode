# https://leetcode.com/problems/maximum-average-subarray-i/

"""
643. Maximum Average Subarray I
Максимальный средний подмассив I

Вам дан целочисленный массив nums,
состоящий из n элементов, и целое число k.

Найти непрерывный подмассив, длина которого равна k
имеющему максимальное среднее значение,
и вернуть это значение.
Любой ответ с ошибкой вычисления меньше 10^-5 будет принят.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation:
Максимальное среднее значение равно (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000


Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
            Runtime: 108ms 20.48%
            Memory: 27.46MB 40.20%
        """
        nums_len = len(nums)
        if nums_len < k:
            return 0

        result = -100000
        left = 0
        cur_sum = 0

        for right in range(0, nums_len):
            cur_sum += nums[right]

            if right == nums_len - 1:
                print()

            if right >= k - 1:
                average = cur_sum / k
                result = max(result, average)

                cur_sum -= nums[left]
                left += 1

                if left > nums_len - k + 1:
                    break

        return result


def tests():
    solution = Solution()

    result = solution.findMaxAverage(
        nums=[7, 4, 5, 8, 8, 3, 9, 8, 7, 6],
        k=7
    )
    assert result == 7.0

    result = solution.findMaxAverage(
        nums=[1, 12, -5, -6, 50, 3],
        k=4
    )
    assert result == 12.75

    result = solution.findMaxAverage(
        nums=[5],
        k=1
    )
    assert result == 5.0


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
