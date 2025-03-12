# https://leetcode.com/problems/string-to-integer-atoi

"""
8. String to Integer (atoi)
Строка в целое число (atoi)

Реализуйте myAtoi(string s)функцию,
которая преобразует строку в 32-битное знаковое целое число.

Алгоритм myAtoi(string s)следующий:

- Пробелы: игнорировать все начальные пробелы ( " ").
- Знак: определите знак, проверив, является ли следующий символ '-'или '+', п
редполагая положительность, если ни один из них отсутствует.
- Преобразование: Прочитайте целое число, пропуская ведущие нули,
пока не встретится нецифровой символ или не будет достигнут конец строки.
Если не было прочитано ни одной цифры, то результатом будет 0.
- Округление: Если целое число выходит за пределы 32-битного знакового целого числа,
 округлите целое число, чтобы оно осталось в пределах диапазона [-2^31, 2^31 - 1].
В частности, целые числа, меньшие -2^31, следует округлить до 2^31 - 1, а целые числа,
большие, следует округлить до  2^31 - 1.

Верните целое число в качестве конечного результата.


Example 1:
Input: s = "42"
Output: 42
Explanation:

Подчеркнутые символы — это то, что считывается, а каретка — текущая позиция считывателя.
Шаг 1: "42" (символы не считываются, так как нет начальных пробелов)
         ^
Шаг 2: "42" (символы не считываются, так как нет ни '-', ни '+')
         ^
Шаг 3: " 42 " (считывается "42")
           ^

Example 2:
Input: s = " -042"
Output: -42
Explanation:
Шаг 1: "    -042" (начальные пробелы считываются и игнорируются)
            ^
Шаг 2: "    - 042" (считывается '-', поэтому результат должен быть отрицательным)
             ^
Шаг 3: " - 042 " (считывается 042, начальные нули в результате игнорируются)
               ^

Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Шаг 1: "1337c0d3" (символы не считываются, так как нет начальных пробелов)
         ^
Шаг 2: "1337c0d3" (символы не считываются, так как нет ни "-", ни "+")
         ^
Шаг 3: " 1337 c0d3" ("считывается "1337"; чтение останавливается,
так как следующий символ не является цифрой)

Example 4:
Input: s = "0-1"
Output: 0
Explanation:

Шаг 1: «0-1» (символы не считываются, так как нет начальных пробелов)
         ^
Шаг 2: «0-1» (символы не считываются, так как нет ни «-», ни «+»)
         ^
Шаг 3: « 0 -1» («считывается «0»; чтение останавливается, так как следующий символ не является цифрой)


Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Чтение останавливается на первом нецифровом символе «w».


Constraints:
0 <= s.length <= 200
s consists of English letters (lower-case and upper-case),
 digits (0-9), ' ', '+', '-', and '.'.
"""


class Solution:
    def __init__(self):
        self.numbers = '0123456789'
        self.min_value = -2 ** 31
        self.max_value = 2 ** 31 - 1

    def myAtoi(self, s: str) -> int:
        """
            Runtime: 0ms 100.00%
            Memory: 17.85MB 48.08%
        """
        s = s.strip()  # Очистка пробелов

        if len(s) == 0:
            return 0

        result = 0
        valid_str = ''
        start = 0

        if s[0] == '-':
            valid_str += '-'
            start += 1
        elif s[0] == '+':
            start += 1

        for symbol in s[start:]:
            if symbol not in self.numbers:
                # Нечисловой символ
                break
            valid_str += symbol

        if valid_str != '':
            try:
                result = int(valid_str)
            except Exception:
                return 0

        if result < self.min_value:
            return self.min_value
        elif result > self.max_value:
            return self.max_value

        return result


def tests():
    solution = Solution()

    result = solution.myAtoi(
        s="-+12"
    )
    assert result == 0

    result = solution.myAtoi(
        s="42"
    )
    assert result == 42

    result = solution.myAtoi(
        s=" -042"
    )
    assert result == -42

    result = solution.myAtoi(
        s="1337c0d3"
    )
    assert result == 1337

    result = solution.myAtoi(
        s="0-1"
    )
    assert result == 0

    result = solution.myAtoi(
        s="words and 987"
    )
    assert result == 0


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
