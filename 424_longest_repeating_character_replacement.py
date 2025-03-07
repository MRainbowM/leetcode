# https://leetcode.com/problems/longest-repeating-character-replacement/
# Скользящее окно
"""
424. Longest Repeating Character Replacement
Самая длинная повторяющаяся замена символа

Вам дана строка s и целое число k.
Вы можете выбрать любой символ строки
и изменить его на любой другой заглавный английский символ.
Эту операцию можно выполнять большинство k раз.

Верните длину самой длинной подстроки,
содержащей ту же букву,
которую вы можете получить после выполнения вышеуказанных операций.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Замените две буквы «A» на две буквы «B» или наоборот.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Замените одну 'A' в середине на 'B' и получите "AABBBBA".
Подстрока "BBBB" имеет самые длинные повторяющиеся буквы, а именно 4.
Могут существовать и другие способы получить этот ответ.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters
(s состоит только из заглавных английских букв)
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Runtime: 135 (52.11%)
        Memory: 17.81 (97.54%)
        """
        left = 0
        max_length = 0
        sting_letter = {}

        for right in range(0, len(s)):
            cur_letter = s[right]

            if cur_letter not in sting_letter.keys():
                sting_letter[cur_letter] = 1
            else:
                sting_letter[cur_letter] += 1

            max_count_letter = max(sting_letter.values())

            len_temp_str = right - left + 1

            if (len_temp_str - k) > max_count_letter:
                sting_letter[s[left]] -= 1
                left += 1
            else:
                max_length = max(len_temp_str, max_length)

        return max_length


def tests():
    solution = Solution()

    result = solution.characterReplacement(
        s="ABAB", k=0
    )
    assert result == 1

    result = solution.characterReplacement(
        s="ABAB", k=2
    )
    assert result == 4

    result = solution.characterReplacement(
        s="AABABBA", k=1
    )
    assert result == 4


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
