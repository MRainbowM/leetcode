# https://leetcode.com/problems/minimum-size-subarray-sum/

"""
209. Minimum Size Subarray Sum
Минимальный размер суммы подмассива

Дан массив положительных целых чисел nums
и положительное целое число target,
вернуть минимальную длину массива.
подмассив сумма которых больше или равна target.
Если такого подмассива нет, верните 0 вместо этого.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation:
Подмассив [4,3] имеет минимальную длину
при ограничении задачи.

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
            Runtime: 9ms 60.91%
            Memory: 28.24MB 80.83%
        """
        nums_len = len(nums)
        min_length = nums_len + 1

        left = 0
        current_sum = 0

        for right in range(0, nums_len):
            current_sum += nums[right]

            if current_sum < target:
                continue

            else:
                min_length = min(min_length, right - left + 1)
                while left < right:
                    current_sum -= nums[left]
                    left += 1

                    if current_sum >= target:
                        min_length = min(min_length, right - left + 1)
                    else:
                        break

        if min_length == nums_len + 1:
            return 0

        return min_length


def tests():
    solution = Solution()

    result = solution.minSubArrayLen(
        target=7,
        nums=[2, 3, 1, 2, 4, 3]
    )
    assert result == 2

    result = solution.minSubArrayLen(
        target=4,
        nums=[1, 4, 4]
    )
    assert result == 1

    result = solution.minSubArrayLen(
        target=11,
        nums=[1, 1, 1, 1, 1, 1, 1, 1]
    )
    assert result == 0


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
