class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i, one, two):
            # Base case: if i == n-1, return 'one'
            if i == n - 1:
                return one
            return climb(i + 1, one + two, one)

        # Edge case: n == 0 or n == 1
        if n == 0 or n == 1:
            return 1

        return climb(0, 1, 1)
