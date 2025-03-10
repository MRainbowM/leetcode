# https://leetcode.com/problems/shifting-letters

"""
848. Shifting Letters
Смещение букв

Вам дана строка s строчных английских букв
и целочисленный массив shifts той же длины.

Назовите shift() букву,
следующую букву в алфавите (переходя так, чтобы 'z' получилось 'a').

Например, shift('a') = 'b', shift('t') = 'u', и shift('z') = 'a'.
Теперь для каждого shifts[i] = x
мы хотим сдвинуть первые i + 1 буквы s, x раз.

Верните окончательную строку после применения всех подобных сдвигов к s.

Example 1:
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: Начинаем с "abc".
После сдвига первой 1 буквы s на 3 получим "dbc".
После сдвига первых 2 букв s на 5 получим "igc".
После сдвига первых 3 букв s на 9 получим "rpl", ответ.

Example 2:
Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"

Ограничения:
1 <= s.length <= 105
sсостоит из строчных английских букв.
shifts.length == s.length
0 <= shifts[i] <= 109
"""
from typing import List


class Solution:
    """
    ord() - возвращает Unicode-код символа
    a → 97
    z → 122
    chr() - возвращает символ по его Unicode-коду
    """

    def __init__(self):
        self.unicode_alphabet_start = 97
        self.unicode_alphabet_end = 122
        self.alphabet_count = 26

    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        """
            Runtime: 116ms 29.04%
            Memory: 29.34MB 49.32%
        """

        def get_idx_by_letter(char: str) -> int:
            return ord(char) - ord('a')

        def get_letter_by_idx(idx: int):
            return chr(idx + ord('a'))

        sum_shifts = sum(shifts) % self.alphabet_count
        result = ''

        # Формирование стартовых индексов букв в строке
        for i, char in enumerate(s):
            # Стартовый индекс
            start_idx = get_idx_by_letter(char)

            new_idx = (start_idx + sum_shifts) % self.alphabet_count
            result += get_letter_by_idx(new_idx)
            sum_shifts = (sum_shifts - shifts[i]) % self.alphabet_count

        return result

    def shiftingLetters_v3(self, s: str, shifts: List[int]) -> str:
        """
            Runtime: 115ms (29.73%)
            Memory: 29.98MB (21.87%)
        """

        def get_idx_by_letter(char: str) -> int:
            # Отсчет с 0
            return ord(char) - ord('a')

        def get_letter_by_idx(idx: int):
            return chr(idx + ord('a'))

        alphabet_index = []
        sum_shifts = sum(shifts) % self.alphabet_count

        # Формирование стартовых индексов букв в строке
        for i, char in enumerate(s):
            # Стартовый индекс
            start_idx = get_idx_by_letter(char)

            res = (start_idx + sum_shifts) % self.alphabet_count
            alphabet_index.append(res)
            sum_shifts = (sum_shifts - shifts[i]) % self.alphabet_count

        result = ''.join([get_letter_by_idx(index) for index in alphabet_index])

        return result

    def shiftingLetters_v2(self, s: str, shifts: List[int]) -> str:
        """
        test 41 Time Limit Exceeded
        """

        def get_idx_by_letter(char: str) -> int:
            # Отсчет с 0
            return ord(char) - ord('a')

        def get_letter_by_idx(idx: int):
            return chr(idx + self.unicode_alphabet_start)

        alphabet_index = []

        # Формирование стартовых индексов букв в строке
        for char in s:
            alphabet_index.append(get_idx_by_letter(char))

        for index, shift in enumerate(shifts):

            for i in range(0, index + 1):
                if shift > self.alphabet_count:
                    shift = shift % self.alphabet_count

                res = alphabet_index[i] + shift
                if res >= self.alphabet_count:
                    res = res - self.alphabet_count

                alphabet_index[i] = res

        result = ''.join([get_letter_by_idx(index) for index in alphabet_index])

        return result

    def shiftingLetters_v1(self, s: str, shifts: List[int]) -> str:
        """
        26 test Time Limit Exceeded
        """
        alphabet_index = []

        # Формирование стартовых индексов букв в строке
        for char in s:
            alphabet_index.append(ord(char))

        for index, shift in enumerate(shifts):

            for i in range(0, index + 1):
                res = alphabet_index[i] + shift

                while res > self.unicode_alphabet_end:
                    res = res - self.unicode_alphabet_end + self.unicode_alphabet_start - 1

                alphabet_index[i] = res

        result = ''.join([chr(index) for index in alphabet_index])

        return result


def tests():
    solution = Solution()

    result = solution.shiftingLetters(
        s="gdhbjaph",
        shifts=[74, 34, 65, 30, 43, 91, 14, 10]
    )
    assert result == "deahllnr"

    result = solution.shiftingLetters(
        s="mkgfzkkuxownxvfvxasy",
        shifts=[505870226, 437526072, 266740649, 224336793, 532917782, 311122363, 567754492, 595798950, 81520022,
                684110326, 137742843, 275267355, 856903962, 148291585, 919054234, 467541837, 622939912, 116899933,
                983296461, 536563513]
    )
    assert result == "wqqwlcjnkphhsyvrkdod"

    result = solution.shiftingLetters(
        s="abc",
        shifts=[3, 5, 9]
    )
    assert result == "rpl"

    result = solution.shiftingLetters(
        s="aaa",
        shifts=[1, 2, 3]
    )
    assert result == "gfd"


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
