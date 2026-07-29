class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]

        for i in range(1, len(prices)):
            prev_cash = cash
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, prev_cash - prices[i])

        return cash