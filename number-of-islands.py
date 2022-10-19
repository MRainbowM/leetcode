# https://leetcode.com/problems/number-of-islands
# Алгоритм поиска в глубину на Python
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        visited = set()
        islands = 0
        h = len(grid)
        w = len(grid[0])

        for i in range(0, h):
            for j in range(0, w):
                if grid[i][j] == '1' and (i, j) not in visited:
                    island = self.dfs(grid, h, w, i, j)
                    islands += 1
                    visited = visited.union(island)

        return islands

    def dfs(self, grid, h, w, i, j, visited=None):
        if visited is None:
            visited = set()
        visited.add((i, j))

        for [di, dj] in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            next_i, next_j = i + di, j + dj

            if (
                    self.within_grid(h, w, next_i, next_j)
                    and grid[next_i][next_j] == '1'
                    and (next_i, next_j) not in visited
            ):
                self.dfs(grid, h, w, next_i, next_j, visited)

        return visited

    def within_grid(self, h, w, i, j):
        return 0 <= i < h and 0 <= j and j < w


def tests():
    solution = Solution()

    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    result = solution.numIslands(grid=grid)
    assert result == 3

    grid = [
        ["1", "1", "1"],
        ["0", "1", "0"],
        ["1", "1", "1"]
    ]

    result = solution.numIslands(grid=grid)
    assert result == 1

    grid = [["1", "0", "1", "1", "0", "1", "1"]]
    result = solution.numIslands(grid=grid)
    assert result == 3

    print("ВСЕ ЧИКИ-ПУКИ!!!")


tests()
