# https://leetcode.com/problems/reverse-words-in-a-string
"""
151. Reverse Words in a String
Перестановка слов в строке

Дана входная строка s, необходимо поменять местами слова.

Слово определяется как последовательность непробельных символов.
Слова в s будут разделены как минимум одним пробелом.

Возвращает строку слов в обратном порядке, соединенных одним пробелом.

Обратите внимание, что s может содержать начальные или конечные пробелы
или несколько пробелов между двумя словами.
Возвращаемая строка должна содержать только один пробел, разделяющий слова.
Не включайте никаких дополнительных пробелов.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation:
Ваша перевернутая строка не должна содержать начальных или конечных пробелов.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation:
Вам необходимо сократить несколько пробелов между двумя словами
до одного пробела в перевернутой строке.

Constraints:

1 <= s.length <= 104
s содержит английские буквы (заглавные и строчные), цифры и пробелы ' '.
В языке есть по крайней мере одно слово s.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """
            Runtime: 0ms 100.00%
            Memory: 17.90MB 69.16%
        """
        string_array = s.split(' ')
        result = ''

        for i in range(len(string_array) - 1, -1, -1):
            if string_array[i] == '':
                continue

            result += string_array[i] + ' '

        result = result[:-1]

        return result


def tests():
    solution = Solution()

    result = solution.reverseWords(
        s="the sky is blue"
    )
    assert result == "blue is sky the"

    result = solution.reverseWords(
        s="  hello world  "
    )
    assert result == "world hello"

    result = solution.reverseWords(
        s="a good   example"
    )
    assert result == "example good a"


if __name__ == "__main__":
    tests()

    print("good")
