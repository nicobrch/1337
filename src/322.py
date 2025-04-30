class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        res = 0
        sum = 0
        aux = amount

        if amount == 0:
            return res

        coins.sort()

        print(f"coins: {coins}")

        for coin in reversed(coins):
            print(f"res: {res} sum: {sum} aux: {aux}")
            if coin == 0 or coin > aux:
                continue

            if aux / coin >= 0:
                res += int(aux/coin)
                sum += coin * int(aux/coin)
                aux = aux % coin

            print(f"res: {res} sum: {sum} aux: {aux}")

        if sum < amount:
            return -1

        return res


sol = Solution()
print(sol.coinChange([186, 419, 83, 408], 6249))
