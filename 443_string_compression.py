# https://leetcode.com/problems/string-compression

"""
443. String Compression
Сжатие строк

Дан массив символов chars,
сожмите его, используя следующий алгоритм:

Начните с пустой строки s.
Для каждой группы последовательных повторяющихся символов в chars:
- Если длина группы равна 1, добавьте символ к s.
- В противном случае добавьте символ, а затем длину группы.

Сжатая строка s не должна возвращаться отдельно,
а вместо этого должна храниться во входном массиве символов chars.
Обратите внимание, что длины групп,
которые равны 10 или больше, будут разделены на несколько символов в chars.

После того, как вы закончите изменять входной массив,
верните новую длину массива.

Вам необходимо написать алгоритм, который использует
только постоянное дополнительное пространство.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Верните 6,
и первые 6 символов входного массива должны быть: ["a","2","b","2","c","3"]
Explanation: Группы — это "aa", "bb" и "ccc". Это сжимается до "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Верните 1, а первый символ входного массива должен быть: ["a"]
Explanation: Единственная группа — это "a",
которая остается несжатой, поскольку это один символ.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Верните 4,
и первые 4 символа входного массива должны быть: ["a","b","1","2"].
Explanation: Группы — это "a" и "bbbbbbbbbbbb". Это сжимается до "ab12".

Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        """
            Runtime: 0ms 100.00%
            Memory: 17.88 MB 74.98%
        """

        def set_count(count: int, start_group: int):
            count_str = str(count)
            start = start_group + 1
            end_group = start_group + count - 1

            for c in count_str:
                chars[start] = c
                start += 1

            while end_group > start - 1:
                chars.pop(end_group)
                end_group -= 1

        chars_len = len(chars)
        cur_letter = chars[-1]

        cur_count = 0

        for left in range(chars_len - 1, -1, -1):
            if cur_letter == chars[left]:
                cur_count += 1

            else:
                if cur_count > 1:
                    set_count(
                        count=cur_count,
                        start_group=left + 1
                    )

                cur_count = 1
                cur_letter = chars[left]

        if cur_count > 1:
            set_count(count=cur_count, start_group=0)

        return len(chars)


def tests():
    solution = Solution()

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    result = solution.compress(
        chars=chars
    )
    assert result == 6
    assert chars == ["a", "2", "b", "2", "c", "3"]

    chars = ["a"]
    result = solution.compress(
        chars=chars
    )
    assert result == 1
    assert chars == ["a"]

    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    result = solution.compress(
        chars=chars
    )
    assert result == 4
    assert chars == ["a", "b", "1", "2"]


if __name__ == "__main__":
    tests()
    print('good')
