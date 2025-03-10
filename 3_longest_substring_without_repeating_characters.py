# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Скользящее окно
"""
3. Longest Substring Without Repeating Characters
Самая длинная подстрока без повторяющихся символов

Дана строка s, найдите длину самой длинной из них подстроки
без повторяющихся символов.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: Ответ: "abc", длина которого равна 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: Ответ: "b", длина которого равна 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: Ответ: "wke" длиной 3.
Обратите внимание, что ответ должен быть подстрокой,
"pwke" — это подпоследовательность, а не подстрока.

Ограничения:
0 <= s.length <= 5 * 104
s состоит из английских букв, цифр, символов и пробелов.
"""


class Solution:
    def lengthOfLongestSubstring_v1(self, s: str) -> int:
        """
            Runtime: 27ms (23.58%)
            Memory: 17.99MB (34.33%)
        """
        max_length = 0
        left = 0
        symbols_in_slice = []

        for right in range(0, len(s)):
            symbol = s[right]

            if symbol in symbols_in_slice:
                # Символ уже есть в подстроке
                for item in symbols_in_slice:
                    if item == symbol:
                        symbols_in_slice = symbols_in_slice[1:]
                        left += 1
                        break

                    symbols_in_slice = symbols_in_slice[1:]
                    left += 1

            symbols_in_slice.append(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            Runtime: 19ms (57.06%)
            Memory: 17.85MB (53.08%)
        """
        max_length = 0
        left = 0
        symbols_in_slice = set()

        for right, symbol in enumerate(s):

            while symbol in symbols_in_slice:
                symbols_in_slice.remove(s[left])
                left += 1

            symbols_in_slice.add(symbol)
            max_length = max(max_length, right - left + 1)

        return max_length


def tests():
    solution = Solution()

    result = solution.lengthOfLongestSubstring(
        s="abcabcbb"
    )
    assert result == 3

    result = solution.lengthOfLongestSubstring(
        s="bbbbb"
    )
    assert result == 1

    result = solution.lengthOfLongestSubstring(
        s="pwwkew"
    )
    assert result == 3


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
