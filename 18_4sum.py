# https://leetcode.com/problems/4sum

"""
18. 4Sum

Учитывая массив nums целых n чисел,
вернуть массив всех уникальных четверок,
[nums[a], nums[b], nums[c], nums[d]] таких, что:

0 <= a, b, c, d < n
a, b, ,c и d различны .
nums[a] + nums[b] + nums[c] + nums[d] == target
Вы можете возвращать ответ в любом порядке .

# 1
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# 2
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

from typing import List


# import itertools
# def _fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#     combinations = list(itertools.combinations(nums, 4))
#     out_list = []
#
#     for combo in combinations:
#         combo_sum = sum(x for x in combo)
#         if combo_sum == target:
#             combo_list = list(combo)
#             combo_list.sort()
#
#             if combo_list not in out_list:
#                 out_list.append(combo_list)
#
#     return out_list


class Solution1:
    def two_sum(self, start: int, target: int) -> None:
        nums = self.nums
        left = start
        right = len(nums) - 1

        while left < right:
            left_value = nums[left]
            right_value = nums[right]
            val = left_value + right_value
            if val < target:
                left += 1
            elif val > target:
                right -= 1
            else:
                self.results.append(self.prefix + [left_value, right_value])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    def k_sum(self, k: int, start: int, target: int) -> None:
        if k == 2:
            self.two_sum(start, target)
            return

        nums = self.nums
        for idx in range(start, len(nums) - k + 1):
            if (
                    # not start
                    idx > start
                    and
                    # not same as prev
                    nums[idx] == nums[idx - 1]
            ):
                continue
            value = nums[idx]
            self.prefix.append(value)
            self.k_sum(k - 1, idx + 1, target - value)
            self.prefix.pop()

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.prefix = []
        self.results = []
        self.k_sum(4, 0, target)
        return self.results


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        len_nums = len(nums)
        result = []

        for i in range(len_nums):

            if i != 0 and nums[i] == nums[i - 1]:
                # индекс не первый, и текущий элемент и предыдущий равны
                continue

            for j in range(i + 1, len_nums):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    # индекс не начальный, и текущий элемент и предыдущий равны
                    continue

                # Далее сумма двух
                left = j + 1
                right = len_nums - 1

                while left < right:
                    temp_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if temp_sum > target:
                        # сумма больше цели,
                        # сдвигаем правый указатель в сторону уменьшения
                        right -= 1
                    elif temp_sum < target:
                        # сумма меньше цели,
                        # сдвигаем левый указатель в сторону увеличения
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        # увеличение левого указателя
                        left += 1

                        while left < right and nums[left] == nums[left - 1]:
                            # пока левый указатель не достиг правого
                            # и текущий элемент равен предыдущему
                            # -> увеличиваем левый указатель
                            left += 1

        return result


def comparison_lists(l1: List[List[int]], l2: List[List[int]]) -> bool:
    if len(l1) != len(l2):
        return False

    l1 = [array.sort() for array in l1]
    l2 = [array.sort() for array in l2]

    for el in l1:
        if el not in l2:
            return False
    return True


def tests():
    solution = Solution()

    result = solution.fourSum(
        nums=[1, 0, -1, 0, -2, 2],
        target=0
    )
    assert comparison_lists(
        result,
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    )

    result = solution.fourSum(
        nums=[2, 2, 2, 2, 2],
        target=8
    )
    assert comparison_lists(
        result,
        [[2, 2, 2, 2]]
    )


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
