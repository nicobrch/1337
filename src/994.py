from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        minutes, fresh = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # count the number of fresh oranges
                if grid[i][j] == 1:
                    fresh += 1

                # add rotten oranges coordinates to the queue
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # iterate while queue is not empty and there are fresh oranges
        while q and fresh > 0:
            for _ in range(len(q)):
                # pop left removes oldest rotten orange
                i, j = q.popleft()

                for move_row, move_col in directions:
                    row, col = move_row + i, move_col + j

                    # if out of bounds, continue
                    if (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) or grid[row][col] != 1):
                        continue

                    # else, make rotten and substract from fresh
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            minutes += 1

        return minutes if fresh == 0 else -1
