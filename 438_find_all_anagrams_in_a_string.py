# https://leetcode.com/problems/find-all-anagrams-in-a-string

"""
438. Find All Anagrams in a String
Найдите все анаграммы в строке

Даны две строки s и p,
вернуть массив всех начальных индексов p строк анаграммы в s.
Вы можете вернуть ответ в любом порядке.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
Подстрока с начальным индексом = 0 — это "cba", что является анаграммой "abc".
Подстрока с начальным индексом = 6 — это "bac", что является анаграммой "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
Подстрока с начальным индексом = 0 — это "ab", что является анаграммой "ab".
Подстрока с начальным индексом = 1 — это "ba", что является анаграммой "ab".
Подстрока с начальным индексом = 2 — это "ab", что является анаграммой "ab".

Ограничения:
1 <= s.length, p.length <= 3 * 104
s и p состоят из строчных английских букв.
"""
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
            Runtime: 39ms (75.46%)
            Memory: 18.3MB (99.19%)
        """
        result = []
        p_len = len(p)
        left = 0
        find_chars = dict()
        current_chars = dict()

        # Генерация целевого словаря, где ключ - буква, значение - количество
        for char in p:
            if char not in find_chars.keys():
                find_chars[char] = 1
            else:
                find_chars[char] += 1

        # Проход окном по переданной строке
        for right, char in enumerate(s):
            if char not in current_chars.keys():
                current_chars[char] = 1
            else:
                current_chars[char] += 1

            # Длина среза равна целевой подстроке
            if right + 1 - left == p_len:
                if find_chars == current_chars:
                    result.append(left)

                # Удаление крайнего левого символа среза из словаря
                if current_chars[s[left]] > 1:
                    current_chars[s[left]] -= 1
                else:
                    current_chars.pop(s[left])

                # Сдвигаем левый указатель окна
                left += 1

        return result


def tests():
    solution = Solution()
    result = solution.findAnagrams(
        s="cbaebabacd",
        p="abc"
    )
    assert set(result) == {0, 6}

    result = solution.findAnagrams(
        s="abab",
        p="ab"
    )
    assert set(result) == {0, 1, 2}


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
