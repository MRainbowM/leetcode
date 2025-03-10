# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced
"""
1653. Minimum Deletions to Make String Balanced
Минимальное количество удалений для сбалансированной строки

Вам дана строка, sсостоящая только из символов 'a'и 'b'

Вы можете удалить любое количество символов s, чтобы сделать s сбалансированным.
Сбалансированным s является тот, у которого нет пары индексов,
такой что (i,j)i < j и s[i] = 'b' и s[j]= 'a'

Возвращает минимальное количество удалений, необходимое для сбалансированного s.

#
Нам дана строка, s содержащая только два символа: 'a'и 'b'.
Наша цель — сделать строку «сбалансированной»,
удалив любое количество символов в строке.
Строка считается «сбалансированной», если нет вхождений,
где a 'b'следует за an 'a'в любой точке строки позже.

Нам нужно найти минимальное количество удалений,
необходимое для балансировки строки.
Другими словами, после всех удалений,
при чтении строки слева направо, если вы видите символ 'b',
 за ним не должно быть никаких других 'a'.

Example 1:
Input: s = "aababbab"
Output: 2
Explanation: Вы можете либо:
удалить символы в позициях 2 и 6 с индексом 0 ("aa b abb a b" -> "aaabbb"), либо
удалить символы в позициях 3 и 6 с индексом 0 ("aab a bb a b" -> "aabbbb").


Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: Единственное решение — удалить первые два символа.


Constraints:
1 <= s.length <= 105
s[i] is 'a' or 'b'.
"""


class Solution:
    def minimumDeletions_v1(self, s: str) -> int:
        """
        test 143 Time Limit Exceeded
        """
        s_len = len(s)
        min_del = s_len

        a_count = 0
        b_count = 0

        right = s_len - 1

        a_count_array = []  # Кол-во a справа от элемента
        b_count_array = []  # Кол-во b слева от элемента

        for left in range(0, s_len):
            a_count_array.insert(0, a_count)  # Вставка в начало списка
            b_count_array.append(b_count)  # Вставка в конец списка

            if s[left] == 'b':
                b_count += 1

            if s[right] == 'a':
                a_count += 1

            right -= 1

        for i in range(0, s_len):
            min_del = min(min_del, a_count_array[i] + b_count_array[i])

        return min_del

    def minimumDeletions_v2(self, s: str) -> int:
        """
            Runtime: 567ms (24.06%)
            Memory: 21.29MB (26.8%)
        """
        s_len = len(s)
        min_del = s_len

        a_count = 0
        a_count_array = [0] * s_len  # Кол-во a справа от элемента

        for j in range(s_len - 1, -1, -1):  # Обратный цикл
            a_count_array[j] = a_count  # Запись справа налево

            if s[j] == 'a':
                a_count += 1

        b_count = 0

        for i in range(0, s_len):

            min_del = min(min_del, a_count_array[i] + b_count)

            if s[i] == 'b':
                b_count += 1

        return min_del

    def minimumDeletions(self, s: str) -> int:
        """
            Runtime: 115ms (96.91%)
            Memory: 18.3MB (41.75%)
        """
        del_count = 0
        b_count = 0
        for item in s:
            if item == 'b':
                b_count += 1
            elif b_count > 0:
                del_count += 1
                b_count -= 1

        return del_count


def tests():
    solution = Solution()

    result = solution.minimumDeletions(
        s="baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"
    )
    assert result == 18

    result = solution.minimumDeletions(
        s="aababbab"
    )
    assert result == 2

    result = solution.minimumDeletions(
        s="bbaaaaabb"
    )
    assert result == 2


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
