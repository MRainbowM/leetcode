# https://leetcode.com/problems/number-of-islands
# runtime:	984 ms, 290 ms
# memory: 16.6 MB, 29.1 MB

class Solution(object):
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0
        h, w = len(grid), len(grid[0])

        for i in range(0, h):
            for j in range(0, w):
                if grid[i][j] == "1":
                    self.dfs(grid, h, w, i, j)
                    islands += 1

        return islands

    def dfs(self, grid, h, w, i, j):
        # Алгоритм поиска в глубину
        # Сложность: O(V). V — общее количество вершин
        grid[i][j] = "0"
        for [di, dj] in self.directions:
            next_i, next_j = i + di, j + dj

            if (
                    self.within_grid(h, w, next_i, next_j)
                    and grid[next_i][next_j] == "1"
            ):
                self.dfs(grid, h, w, next_i, next_j)

    def within_grid(self, h, w, i, j):
        return 0 <= i < h and 0 <= j < w


def tests():
    solution = Solution()

    # 1
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    result = solution.numIslands(grid=grid)
    assert result == 3

    # 2
    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]

    result = solution.numIslands(grid=grid)
    assert result == 1

    # 3
    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    result = solution.numIslands(grid=grid)
    assert result == 3

    # 4
    grid = [
        ["0", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["1", "0", "0", "1", "1"]
    ]
    result = solution.numIslands(grid=grid)
    assert result == 4

    print("ВСЕ ЧИКИ-ПУКИ!!!")


tests()
