# https://leetcode.com/problems/interval-list-intersections

"""
986. Interval List Intersections
Пересечения интервального списка

Вам даны два списка закрытых интервалов,
first List и second List.
Каждый список интервалов попарно не пересекается и отсортирован в порядке
firstList[i] = [starti, endi]
secondList[j] = [startj, endj]

Верните пересечение этих двух интервальных списков.

Замкнутый интервал [a, b] (с a <= b)
обозначает множество действительных чисел xс a <= x <= b.

Пересечение двух замкнутых интервалов —
это множество действительных чисел,
которые либо пусты,
либо представлены в виде замкнутого интервала.
Например, пересечение [1, 3] и [2, 4]равно [2, 3].

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]],
secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Constraints:
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 109
endi < starti+1
0 <= startj < endj <= 109
endj < startj+1
"""
from typing import List


class Solution:
    def intervalIntersection(
            self,
            firstList: List[List[int]],
            secondList: List[List[int]]
    ) -> List[List[int]]:
        """
            Runtime: 455ms 5.15%
            Memory: 18.48MB 1.55%
        """
        result = []

        for first_item in firstList:

            for second_item in secondList:

                if (
                        (second_item[0] <= first_item[1] <= second_item[1]) or
                        (second_item[0] <= first_item[0] <= second_item[1]) or
                        (first_item[0] <= second_item[0] <= first_item[1]) or
                        (first_item[0] <= second_item[1] <= first_item[1])
                ):
                    # Первая правая граница во втором интервале
                    start = second_item[0] if second_item[0] > first_item[0] else first_item[0]
                    end = second_item[1] if second_item[1] < first_item[1] else first_item[1]
                    result.append([start, end])

                if second_item[0] > first_item[1]:
                    break

        return result


def tests():
    solution = Solution()

    result = solution.intervalIntersection(
        firstList=[[3, 5], [9, 20]],
        secondList=[[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    )
    assert result == [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]

    result = solution.intervalIntersection(
        firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
        secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]
    )
    assert result == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]

    result = solution.intervalIntersection(
        firstList=[[1, 3], [5, 9]], secondList=[]
    )
    assert result == []


if __name__ == "__main__":
    tests()
    print('good')
