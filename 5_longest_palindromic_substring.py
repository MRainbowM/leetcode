# https://leetcode.com/problems/longest-palindromic-substring
"""
5. Longest Palindromic Substring
Самая длинная палиндромная подстрока

Дана строка s, вернуть самую длинную палиндромный подстрока в s.

Строка является палиндромной,
если она одинаково читается слева направо и слева направо.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" также является допустимым ответом.

Example 2:
Input: s = "cbbd"
Output: "bb"

Ограничения:
1 <= s.length <= 1000
s состоят только из цифр и английских букв.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
            Runtime: 3387ms 18.18%
            Memory: 17.74MB 84.50%
        """

        def check_palindrome(cur_start, cur_length) -> bool:
            left = cur_start
            right = cur_length - 1

            while left < right:
                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1
            return True

        for length in range(len(s), 0, -1):

            for start in range(0, len(s) - length + 1):
                is_palindrome = check_palindrome(
                    cur_start=start,
                    cur_length=start + length
                )
                if is_palindrome:
                    result = s[start: start + length]
                    return result

        return ''


def tests():
    solution = Solution()

    result = solution.longestPalindrome(
        s="babad"
    )
    assert result in ["bab", "aba"]

    result = solution.longestPalindrome(
        s="cbbd"
    )
    assert result in ["bb"]


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
