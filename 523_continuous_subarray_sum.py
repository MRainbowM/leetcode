# https://leetcode.com/problems/continuous-subarray-sum/description/

"""
523. Continuous Subarray Sum

Дан целочисленный массив nums и целое число k,
вернуть, true если nums есть хороший подмассив,
или false в противном случае.

Хороший подмассив — это подмассив, в котором:

его длина составляет не менее двух, и
сумма элементов подмассива кратна k.
Обратите внимание, что:

Подмассив — это непрерывная часть массива.
Целое число x является кратным k,
если k существует целое число,
n такое что x = n * k. 0 всегда кратно k

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] — это непрерывный подмассив размера 2,
сумма элементов которого равна 6.

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] — это непрерывный подмассив размера 5,
сумма элементов которого составляет 42.
42 кратно 6, поскольку 42 = 7 * 6, а 7 — целое число.

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        Runtime: 47ms
        Memory: 32.02MB
        """
        prefix_mod = 0
        mod_seen = {0: -1}

        for i in range(0, len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in mod_seen:
                size = i - mod_seen[prefix_mod]
                if abs(size) >= 2:
                    return True
            else:
                mod_seen[prefix_mod] = i

        return False


def tests():
    solution = Solution()

    result = solution.checkSubarraySum(
        nums=[2,4,3],
        k=6
    )
    assert result is True


    result = solution.checkSubarraySum(
        nums=[23, 2, 4, 6, 7],
        k=6
    )
    assert result is True

    result = solution.checkSubarraySum(
        nums=[23, 2, 6, 4, 7],
        k=6
    )
    assert result is True

    result = solution.checkSubarraySum(
        nums=[23, 2, 6, 4, 7],
        k=13
    )
    assert result is False


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
