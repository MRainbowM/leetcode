# https://leetcode.com/problems/continuous-subarrays/

"""
2762. Continuous Subarrays
(Непрерывные подмассивы)

Вам дан целочисленный массив с индексом 0 nums.
Подмассив nums называется непрерывным, если:

    Пусть i, i + 1, ..., j — индексы в подмассиве.
    Тогда для каждой пары индексов i <= i1, i2 <= j
    0 <= |nums[i1] - nums[i2]| <= 2

Верните общее количество непрерывных подмассивов.
Подмассив — это непрерывная непустая последовательность элементов внутри массива.

# 1
Input: nums = [5,4,2,4]
Output: 8
Explanation:
Непрерывный подмассив размера 1: [5], [4], [2], [4].
Непрерывный подмассив размера 2: [5,4], [4,2], [2,4].
Непрерывный подмассив размера 3: [4,2,4].
Нет подмассивов размера 4.
Общее количество непрерывных подмассивов = 4 + 3 + 1 = 8.
Можно показать, что больше нет непрерывных подмассивов.


# 2
Input: nums = [1,2,3]
Output: 6
Explanation:
Непрерывный подмассив размера 1: [1], [2], [3].
Непрерывный подмассив размера 2: [1,2], [2,3].
Непрерывный подмассив размера 3: [1,2,3].
Всего непрерывных подмассивов = 3 + 2 + 1 = 6.
"""
from typing import List

from line_profiler_pycharm import profile


class Solution:
    def continuousSubarrays1(self, nums: List[int]) -> int:
        len_nums = len(nums)
        out = len_nums

        for n in range(len_nums):
            temp_min = nums[n]
            temp_max = nums[n]

            for m in range(n + 1, len_nums):

                if (
                        -2 <= temp_min - nums[m] <= 2 and
                        -2 <= temp_max - nums[m] <= 2
                ):
                    out += 1

                    temp_min = min(nums[m], temp_min)
                    temp_max = max(nums[m], temp_max)

                else:
                    break

        return out

    @profile
    def continuousSubarrays2(self, nums: List[int]) -> int:
        """Вылетает по рантайму 325000 s"""
        len_nums = len(nums)

        total_min = min(nums)
        total_max = max(nums)
        if total_max - total_min <= 2:
            return round(len_nums * (len_nums + 1) / 2)

        out = len_nums

        for start in range(len_nums - 1):
            end = start + 2
            while end <= len_nums:
                temp_arr = nums[start:end]
                # print(temp_arr)

                if (
                        -2 <= min(temp_arr) - max(temp_arr) <= 2
                ):
                    out += 1
                    end += 1
                else:

                    break

        return out

    @profile
    def continuousSubarrays3(self, nums: List[int]) -> int:
        """205000 s"""
        len_nums = len(nums)

        nums_set = set(nums)
        total_min = min(nums_set)
        total_max = max(nums_set)
        if total_max - total_min <= 2:
            return round(len_nums * (len_nums + 1) / 2)

        correct, start, prev_end = 0, 0, 0

        for end in range(1, len_nums + 1):

            temp_arr = nums[start:end]
            if max(temp_arr) - min(temp_arr) > 2:

                array_len = end - start - 1
                plus = array_len * (array_len + 1) / 2
                correct += plus
                # print(correct)

                if prev_end > 0:
                    exclude_arr_len = prev_end - start
                    exclude = exclude_arr_len * (exclude_arr_len + 1) / 2
                    # print(-exclude)
                    correct -= exclude

                prev_end = end - 1

                if end < len_nums + 1:
                    prev = None

                    while True:
                        start += 1

                        if prev is not None and prev == nums[start]:
                            continue

                        prev = nums[start]

                        temp_arr = nums[start:end]
                        if max(temp_arr) - min(temp_arr) <= 2:
                            break

            if end == len_nums:
                array_len = end - start
                plus = array_len * (array_len + 1) / 2
                correct += plus

                # print(plus)

                if prev_end > 0:
                    exclude_arr_len = prev_end - start
                    exclude = exclude_arr_len * (exclude_arr_len + 1) / 2
                    # print(-exclude)
                    correct -= exclude

        return round(correct)

    def continuousSubarrays(self, nums: List[int]) -> int:
        """205000 s"""
        len_nums = len(nums)



        correct, start, prev_end = 0, 0, 0

        temp_min = nums[start]
        temp_max = nums[start]
        prev_el = nums[start]

        for end in range(1, len_nums):
            if prev_el == nums[end]:
                continue

            prev_el = nums[end]

            if nums[end] < temp_min:
                temp_min = nums[end]

            if nums[end] > temp_max:
                temp_max = nums[end]

            if temp_max - temp_min > 2:

                array_len = end - start - 1
                plus = array_len * (array_len + 1) / 2
                correct += plus
                # print(correct)

                if prev_end > 0:
                    exclude_arr_len = prev_end - start
                    exclude = exclude_arr_len * (exclude_arr_len + 1) / 2
                    # print(-exclude)
                    correct -= exclude

                prev_end = end - 1

                if end < len_nums - 1:
                    prev = None

                    while True:
                        start += 1

                        if prev is not None and prev == nums[start]:
                            continue

                        prev = nums[start]

                        temp_arr = nums[start:end+1]
                        if max(temp_arr) - min(temp_arr) <= 2:
                            break

            if end == len_nums - 1:
                array_len = end - start
                plus = array_len * (array_len + 1) / 2
                correct += plus

                # print(plus)

                if prev_end > 0:
                    exclude_arr_len = prev_end - start
                    exclude = exclude_arr_len * (exclude_arr_len + 1) / 2
                    # print(-exclude)
                    correct -= exclude

        return round(correct)


def tests():
    solution = Solution()

    result = solution.continuousSubarrays(
        nums=[42, 41, 42, 41, 41, 40, 39, 38]
    )

    assert result == 28

    result = solution.continuousSubarrays(
        nums=[35, 35, 36, 37, 36, 37, 38, 37, 38]
    )

    assert result == 39

    result = solution.continuousSubarrays(
        nums=[65, 66, 67, 66, 66, 65, 64, 65, 65, 64]
    )

    assert result == 43

    result = solution.continuousSubarrays(nums=[5, 4, 2, 4])
    assert result == 8

    result = solution.continuousSubarrays(nums=[1, 2, 3])
    assert result == 6


if __name__ == "__main__":
    tests()

    print("ВСЕ ОК!!!")
