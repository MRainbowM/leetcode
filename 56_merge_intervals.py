# https://leetcode.com/problems/merge-intervals
"""
56. Merge Intervals
Слияние интервалов

Дан массив intervals
где объединить все перекрывающиеся интервалы
и вернуть массив неперекрывающихся интервалов,
которые покрывают все интервалы
во входных данных intervals[i] = [start i, end i]

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Поскольку интервалы [1,3] и [2,6] перекрываются,
объединим их в [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation:
Интервалы [1,4] и [4,5] считаются перекрывающимися.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= start i <= end i <= 104
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            Runtime: 7ms 73.15%
            Memory: 21.67MB 29.13%
        """
        if len(intervals) == 1:
            return intervals

        intervals.sort()

        result = []

        start, end = -1, -1

        for index, interval in enumerate(intervals):

            if start == end == -1:
                start = interval[0]
                end = interval[1]
                continue

            if interval[0] <= end:
                start = interval[0] if interval[0] < start else start
                end = interval[1] if interval[1] > end else end

            else:
                result.append([start, end])
                start, end = interval[0], interval[1]

            if index == len(intervals) - 1:
                result.append([start, end])

        return result


def tests():
    solution = Solution()

    result = solution.merge(
        intervals=[[1, 4], [0, 2], [3, 5]]
    )
    assert result == [[0, 5]]

    result = solution.merge(
        intervals=[[1, 4], [0, 0]]
    )
    assert result == [[0, 0], [1, 4]]

    result = solution.merge(
        intervals=[[1, 4], [0, 1]]
    )
    assert result == [[0, 4]]

    result = solution.merge(
        intervals=[[1, 4], [0, 4]]
    )
    assert result == [[0, 4]]

    result = solution.merge(
        intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]
    )
    assert result == [[1, 6], [8, 10], [15, 18]]

    result = solution.merge(
        intervals=[[1, 4], [4, 5]]
    )
    assert result == [[1, 5]]


if __name__ == "__main__":
    tests()

    print("ВСЕ ЧИКИ-ПУКИ!!!")
