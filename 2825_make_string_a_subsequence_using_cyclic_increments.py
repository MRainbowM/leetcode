# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments

"""
2825. Make String a Subsequence Using Cyclic Increments
(Сделать строку подпоследовательностью с помощью циклических приращений)

Вам даны две строки с индексом 0 str1 и str2.

В операции вы выбираете набор индексов в str1,
и для каждого индекса i в наборе циклически str1[i]
увеличивается до следующего символа.
То есть 'a' становится 'b', 'b' становится 'c', и так далее,
и 'z' становится 'a'.

Возвращает true, если возможно создать str2 подпоследовательность,
str1 выполнив операцию не более одного раза,
в false противном случае.

Примечание: Подпоследовательность строки — это новая строка,
которая образована из исходной строки
путем удаления некоторых (возможно, ни одного) символов
без нарушения относительного положения оставшихся символов.

# 1
Input: str1 = "abc", str2 = "ad"
Output: true
Explanation: Выберите индекс 2 в str1.
    Увеличьте str1[2], чтобы получить «d».
    Следовательно, str1 становится "abd",
    а str2 теперь является подпоследовательностью.
    Поэтому возвращается true.

# 2
Input: str1 = "zc", str2 = "ad"
Output: true
Explanation: Выберите индексы 0 и 1 в str1.
    Увеличьте str1[0], чтобы получить «a».
    Увеличьте str1[1], чтобы получить «d».
    Следовательно, str1 становится "ad",
    а str2 теперь является подпоследовательностью.
    Поэтому возвращается true.

# 3
Input: str1 = "ab", str2 = "d"
Output: false
Explanation: В этом примере можно показать,
    что невозможно сделать str2 подпоследовательностью str1,
    используя операцию не более одного раза.
    Следовательно, возвращается false.

Ограничения:

1 <= str1.length <= 105
1 <= str2.length <= 105
str1 и str2 состоят только из строчных английских букв.

"""


class Solution:
    def __init__(self):
        self.abc_dict = {
            'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'e',
            'e': 'f',
            'f': 'g',
            'g': 'h',
            'h': 'i',
            'i': 'j',
            'j': 'k',
            'k': 'l',
            'l': 'm',
            'm': 'n',
            'n': 'o',
            'o': 'p',
            'p': 'q',
            'q': 'r',
            'r': 's',
            's': 't',
            't': 'u',
            'u': 'v',
            'v': 'w',
            'w': 'x',
            'x': 'y',
            'y': 'z',
            'z': 'a'
        }

    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        if len(str2) > len(str1):
            # str2 не может быть подстрокой str1,
            # если она длиннее
            return False

        for let2 in str2:
            temp_state = False

            for idx, let1 in enumerate(str1):
                if let1 == let2 or let2 == self.abc_dict[let1]:
                    str1 = str1[idx + 1:]

                    temp_state = True
                    break
            if not temp_state:
                return False

        return True


def tests():
    solution = Solution()

    result = solution.canMakeSubsequence(str1='abc', str2='ad')
    assert result is True

    result = solution.canMakeSubsequence(str1='zc', str2='ad')
    assert result is True

    result = solution.canMakeSubsequence(str1='ab', str2='d')
    assert result is False


if __name__ == "__main__":
    tests()

    print("ВСЕ ОК!!!")
