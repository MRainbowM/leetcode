# https://leetcode.com/problems/count-number-of-nice-subarrays

"""
1248. Count Number of Nice Subarrays
Подсчет количества подмассивов Nice

Дан массив целых чисел nums и целое число k.
Непрерывный подмассив называется хорошим, если в нем есть k нечетные числа.

Возвращает количество подмассивов nice.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: Единственные подмассивы с 3 нечетными числами — это [1,1,2,1] и [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: В массиве нет нечетных чисел.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
            Runtime: 72ms 83.58%
            Memory: 23.08MB 56.90%
        """
        left, middle, result, current_sum = 0, 0, 0, 0

        for right in range(0, len(nums)):
            # Если число нечетное, то сумма наращивается иначе - нет
            current_sum += nums[right] % 2

            while current_sum > k:
                # Нечетных чисел больше, чем нужно,
                # сдвигаются левый и средний указатели
                current_sum -= nums[left] % 2
                left += 1
                middle = left

            if current_sum == k:
                # Увеличиваем кол-во подмассивов

                # Сдвигаем средний указатель до первого нечетного числа
                while nums[middle] % 2 == 0:
                    middle += 1

                result += middle - left + 1

        return result


def tests():
    solution = Solution()

    result = solution.numberOfSubarrays(
        nums=[1, 1, 2, 1, 1], k=3
    )
    assert result == 2

    result = solution.numberOfSubarrays(
        nums=[2, 4, 6], k=1
    )
    assert result == 0

    result = solution.numberOfSubarrays(
        nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2
    )
    assert result == 16


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
