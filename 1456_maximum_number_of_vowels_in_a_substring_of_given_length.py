# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description

"""
1456. Maximum Number of Vowels in a Substring of Given Length
1456. Максимальное количество гласных в подстроке заданной длины

Для заданной строки s и целого числа k
вернуть максимальное количество гласных букв
в любой подстроке s длины k.

Гласные буквы в английском языке — это 'a', 'e', 'i', 'o', и 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: Подстрока "iii" содержит 3 гласные буквы.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Любая подстрока длины 2 содержит 2 гласные.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" и "ode" содержат 2 гласные.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""


class Solution:
    def __init__(self):
        self.vowels_array = ['a', 'e', 'i', 'o', 'u']
        self.vowels = 'aeiou'

    def maxVowels(self, s: str, k: int) -> int:
        """
            Runtime: 83ms
            Memory: 18.2MB
        """
        len_s = len(s)
        max_count = 0

        if k > len_s:
            return max_count

        left = 0
        current_count = 0

        for right in range(0, len_s):
            if s[right] in self.vowels:
                current_count += 1

            if right >= k - 1:
                max_count = max(max_count, current_count)

                if s[left] in self.vowels:
                    current_count -= 1

                if max_count == k:
                    return k

                left += 1

        return max_count

    def maxVowels_v2(self, s: str, k: int) -> int:
        """
            Runtime: 91ms
            Memory: 18.87MB
        """
        len_s = len(s)
        max_count = 0

        if k > len_s:
            return max_count

        left = 0
        right = k

        slice = s[left: right]
        current_count = k - len(''.join([letter for letter in slice if letter not in self.vowels]))
        max_count = current_count
        if max_count == k:
            return k

        left += 1
        right += 1

        while right <= len_s:
            prev_is_vowel = s[left - 1] in self.vowels
            last_is_vowel = s[right - 1] in self.vowels

            current_count = current_count - 1 if prev_is_vowel else current_count
            current_count = current_count + 1 if last_is_vowel else current_count
            max_count = max(current_count, max_count)

            if max_count == k:
                return max_count

            left += 1
            right += 1

        return max_count

    def maxVowels_v1(self, s: str, k: int) -> int:
        """
        Time Limit Exceeded test 100
        """

        def filter_by_vowels(x: str) -> bool:
            if x in self.vowels_array:
                return True
            return False

        len_s = len(s)
        max_count = 0

        if k > len_s:
            return max_count

        left = 0
        right = k

        while right <= len_s:
            slice = s[left: right]
            vowels_count = len(list(filter(filter_by_vowels, slice)))
            max_count = max(vowels_count, max_count)

            if max_count == k:
                return max_count

            left += 1
            right += 1

        return max_count


def tests():
    solution = Solution()

    result = solution.maxVowels(
        s="ibpbhixfiouhdljnjfflpapptrxgcomvnb",
        k=33
    )
    assert result == 7

    result = solution.maxVowels(
        s="a",
        k=1
    )
    assert result == 1

    result = solution.maxVowels(
        s="aeiou",
        k=2
    )
    assert result == 2

    result = solution.maxVowels(
        s="abciiidef",
        k=3
    )
    assert result == 3

    result = solution.maxVowels(
        s="aeiou",
        k=2
    )
    assert result == 2

    result = solution.maxVowels(
        s="leetcode",
        k=3
    )
    assert result == 2


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
