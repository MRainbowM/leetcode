# https://leetcode.com/problems/concatenation-of-array/

"""
1929. Concatenation of Array

Учитывая целочисленный массив nums длины n,
вы хотите создать массив ans длины 2n,
где ans[i] == nums[i]и ans[i + n] == nums[i]for 0 <= i < n( 0-indexed ).

В частности, ans - это объединение двух nums массивов.

Вернуть массив ans .

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]


Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums
