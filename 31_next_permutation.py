# https://leetcode.com/problems/next-permutation/description/

"""
31. Next Permutation

Перестановка массива целых чисел — это расположение его элементов
в последовательности или линейном порядке.

Например, для arr = [1,2,3],
ниже приведены все перестановки arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
Следующая перестановка массива целых чисел —
это следующая лексикографически большая перестановка его целого числа.
Более формально, если все перестановки массива отсортированы в одном контейнере
в соответствии с их лексикографическим порядком,
то следующая перестановка этого массива — это перестановка,
которая следует за ней в отсортированном контейнере.
Если такое расположение невозможно, массив должен быть переупорядочен
в самом низком возможном порядке (т. е. отсортирован в порядке возрастания).

Например, следующая перестановка arr = [1,2,3]— [1,3,2].
Аналогично, следующая перестановка arr = [2,3,1]— [3,1,2].
В то время как следующая перестановка arr = [3,2,1]
заключается [1,2,3]в том, что [3,2,1]не имеет лексикографически большей перестановки.
Дан массив целых чисел nums. Найдите следующую перестановку nums.

Замена должна быть на месте и использовать только постоянную дополнительную память.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Runtime: 0ms
        Memory: 17.66MB
        """

        def array_reverse(start: int):
            left_idx = start
            right_idx = len(nums) - 1

            while right_idx > left_idx:
                nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

                left_idx += 1
                right_idx -= 1

        first_idx = -1
        two_idx = -1
        nums_len = len(nums)

        for i in range(nums_len - 1, 0, -1):
            prev_item = nums[i - 1]
            curr_item = nums[i]

            if curr_item <= prev_item:
                continue
            else:
                first_idx = i - 1
                break

        if first_idx == -1:
            nums.sort()
            return

        if first_idx == nums_len - 1:
            two_idx = first_idx - 1
        else:
            for j in range(first_idx + 1, nums_len):
                if nums[first_idx] >= nums[j]:
                    two_idx = j - 1
                    break

        nums[first_idx], nums[two_idx] = nums[two_idx], nums[first_idx]
        array_reverse(start=first_idx + 1)


def tests():
    solution = Solution()

    nums = [5, 1, 1]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [1, 1, 5]

    nums = [1, 5, 1]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [5, 1, 1]

    nums = [2, 3, 1]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [3, 1, 2]

    nums = [1, 3, 2]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [2, 1, 3]

    nums = [1, 2]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [2, 1]

    nums = [1, 2, 3]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [1, 3, 2]

    nums = [3, 2, 1]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [1, 2, 3]

    nums = [1, 1, 5]
    solution.nextPermutation(
        nums=nums
    )
    assert nums == [1, 5, 1]


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
