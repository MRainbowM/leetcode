# https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i

"""
2554. Maximum Number of Integers to Choose From a Range I

Вам дан массив целых чисел banned и два целых числа n и maxSum.
Вы выбираете некоторое количество целых чисел,
следуя следующим правилам:

- Выбранные целые числа должны находиться в диапазоне [1, n].
- Каждое целое число может быть выбрано не более одного раза.
- Выбранные целые числа не должны быть в массиве banned.
- Сумма выбранных целых чисел не должна превышать maxSum.

Верните максимальное количество целых чисел,
которые вы можете выбрать, следуя указанным правилам.

# 1
Input: banned = [1,6,5], n = 5, maxSum = 6
Output: 2
Explanation: Вы можете выбрать целые числа 2 и 4.
    2 и 4 находятся в диапазоне [1, 5],
    оба не встречались в banned, а их сумма равна 6,
    что не превышает maxSum.

# 2
Input: banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1
Output: 0
Explanation: Вы не можете выбрать ни одно целое число,
    соблюдая указанные условия.

# 3
Input: banned = [11], n = 7, maxSum = 50
Output: 7
Explanation: Вы можете выбрать целые числа 1, 2, 3, 4, 5, 6 и 7.
    Они находятся в диапазоне [1, 7],
    все они не встречаются в banned,
    а их сумма равна 28, что не превышает maxSum.
"""
from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        temp_sum = 0
        count = 0
        for i in range(1, n + 1):
            if i in banned:
                continue

            if temp_sum + i <= maxSum:
                temp_sum += i
                count += 1
            else:
                break

        return count


def tests():
    solution = Solution()

    result = solution.maxCount(
        banned=[1, 6, 5],
        n=5,
        maxSum=6
    )
    assert result == 2

    result = solution.maxCount(
        banned=[1, 2, 3, 4, 5, 6, 7],
        n=8,
        maxSum=1
    )
    assert result == 0

    result = solution.maxCount(
        banned=[11],
        n=7,
        maxSum=50
    )
    assert result == 7


if __name__ == "__main__":
    tests()

    print("ВСЕ ОК!!!")
