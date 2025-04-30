class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0

        coins.sort()

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for num in range(1, amount + 1):
            for coin in coins:
                if num - coin >= 0:
                    dp[num] = min(dp[num], 1 + dp[num-coin])

        return dp[amount] if dp[amount] != amount + 1 else -1
