# https://leetcode.com/problems/max-number-of-k-sum-pairs

"""
1679. Max Number of K-Sum Pairs
Максимальное количество пар K-сумм

Вам дан массив целых чисел nums и целое число k.

За одну операцию можно выбрать из массива два числа,
сумма которых равна k и удалить их из массива.

Возвращает максимальное количество операций,
которые можно выполнить над массивом.

Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation:  Начинаем с nums = [1,2,3,4]:
- Удалим числа 1 и 4, затем nums = [2,3]
- Удалим числа 2 и 3, затем nums = []
Больше нет пар, которые в сумме дают 5,
следовательно, всего 2 операции.

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Начинаем с nums = [3,1,3,4,3]:
- Удалим первые две тройки, затем nums = [1,4,3]
Больше нет пар, которые в сумме дают 6,
следовательно, всего 1 операция.


Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 109
"""
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        """
            Runtime:497 ms 81.93%
            Memory: 29.85MB 78.25%
        """
        if k == 1:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0

        while left < right:
            cur_sum = nums[left] + nums[right]

            if cur_sum < k:
                left += 1
            elif cur_sum > k:
                right -= 1
            else:
                result += 1
                left += 1
                right -= 1

        return result

    def maxOperations_v1(self, nums: List[int], k: int) -> int:
        """
            test 39 Time Limit Exceeded
        """
        if k == 1:
            return 0

        result = 0
        use_idx = []

        for left in range(0, len(nums) - 1):
            if nums[left] >= k:
                continue
            if left in use_idx:
                continue

            find_num = k - nums[left]

            for right in range(left + 1, len(nums)):
                if right in use_idx:
                    continue

                if nums[right] == find_num:
                    result += 1
                    use_idx.append(right)
                    break

        return result


def tests():
    solution = Solution()

    result = solution.maxOperations(
        nums=[1, 2, 3, 4], k=5
    )
    assert result == 2

    result = solution.maxOperations(
        nums=[3, 1, 3, 4, 3], k=6
    )
    assert result == 1


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
