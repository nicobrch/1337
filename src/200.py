class Solution(object):
    def numIslands(self, grid):
        """

        :type grid: List[List[str]]

        :rtype: int

        """

        count = 0

        if not grid:
            return 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return

            if grid[row][col] != "1":
                return

            if grid[row][col] == "1":
                grid[row][col] = "#"

            dfs(row-1, col)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row, col+1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count
