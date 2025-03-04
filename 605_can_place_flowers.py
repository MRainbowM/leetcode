# https://leetcode.com/problems/can-place-flowers/description/

"""
605. Can Place Flowers

У вас есть длинная клумба,
в которой некоторые участки засажены, а некоторые нет.
Однако цветы нельзя сажать на соседних участках.

Дан целочисленный массив, flowerbed содержащий 0' и 1',
где 0 означает пустой, а 1 означает непустой, и целое число n,
вернуть, можно true ли n посадить новые цветы в flowerbed
не нарушая правила отсутствия смежных цветов, и false в противном случае.

# 1
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

# 2
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""
from typing import List


class Solution:
    def canPlaceFlowers_v1(self, flowerbed: List[int], n: int) -> bool:
        """
        Runtime: 25ms
        Memory: 18.08MB
        """
        if n == 0:
            return True

        flowerbed_len = len(flowerbed)

        if set(flowerbed[0:2]) == {0}:
            n -= 1
            flowerbed[0] = 1

        left = 1
        right = 3

        if n == 0:
            return True

        while right < flowerbed_len:
            if set(flowerbed[left:right + 1]) == {0}:
                n -= 1
                flowerbed[left + 1] = 1
                left += 1
                right += 1

            if n == 0:
                return True

            left += 1
            right += 1

        if set(flowerbed[flowerbed_len - 2: flowerbed_len]) == {0}:
            n -= 1
            if n == 0:
                return True

        return False

    def canPlaceFlowers_v2(self, flowerbed: List[int], n: int) -> bool:
        """
        Runtime: 27ms
        Memory: 18.37MB
        """
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        flowerbed_len = len(flowerbed)

        left = 0
        right = 3

        while right <= flowerbed_len:
            if set(flowerbed[left:right]) == {0}:
                n -= 1
                flowerbed[left + 1] = 1
                left += 1
                right += 1

            if n == 0:
                return True

            left += 1
            right += 1

        return False

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        Runtime: 18ms
        Memory: 18.07MB
        """
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        flowerbed_len = len(flowerbed)

        for i in range(1, flowerbed_len - 1):
            sum_flowers = sum(flowerbed[i - 1:i + 2])
            if sum_flowers == 0:
                flowerbed[i] = 1
                n -= 1
            if n == 0:
                return True

        return False


def tests():
    solution = Solution()

    result1 = solution.canPlaceFlowers(
        flowerbed=[0, 0, 0, 0, 1],
        n=2
    )
    assert result1 is True

    result2 = solution.canPlaceFlowers(
        flowerbed=[1, 0],
        n=1
    )
    assert result2 is False

    result3 = solution.canPlaceFlowers(
        flowerbed=[1, 0, 0, 0, 1, 0, 0],
        n=2
    )
    assert result3 is True

    result4 = solution.canPlaceFlowers(
        flowerbed=[1, 0, 0, 0, 0, 1],
        n=2
    )
    assert result4 is False

    # 1
    result5 = solution.canPlaceFlowers(
        flowerbed=[1, 0, 0, 0, 1],
        n=1
    )
    assert result5 is True

    # 3
    result6 = solution.canPlaceFlowers(
        flowerbed=[1, 0, 0, 0, 1],
        n=2
    )
    assert result6 is False


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
