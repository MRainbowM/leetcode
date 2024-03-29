# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

"""
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers

Десятичное число называется двоично-десятичным,
если каждая его цифра равна 0 или 1 без нулей в начале.
Например, 101 и 1100 являются двоично-десятичным, а 112 и 3001 — нет.


Для заданной строки n, представляющей положительное десятичное целое число,
вернуть минимальное количество положительных двоично-десятичных чисел,
необходимое для того, чтобы их сумма давала n.


Example 1:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32


Example 2:
Input: n = "82734"
Output: 8


Example 3:
Input: n = "27346209830709182346"
Output: 9
"""


class Solution:
    def minPartitions(self, n: str) -> int:
        """
        Максимальная цифра в числе = минимально столько раз нужно отнять двоичное число
        """
        return int(max(n))
        # count_nums = 0
        # while True:
        #     new_n = ''
        #
        #     for num in n:
        #         if num != '0':
        #             new_n += str(int(num) - 1)
        #         else:
        #             new_n += '0'
        #
        #     count_nums += 1
        #
        #     if int(new_n) == 0:
        #         break
        #     n = new_n
        #
        # return count_nums


def tests():
    solution = Solution()

    result = solution.minPartitions(n='32')
    assert result == 3

    result = solution.minPartitions(n='82734')
    assert result == 8

    result = solution.minPartitions(n='27346209830709182346')
    assert result == 9

    print("ВСЕ ЧИКИ-ПУКИ!!!")


tests()
