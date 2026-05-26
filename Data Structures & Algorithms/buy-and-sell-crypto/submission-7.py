class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        m = 0

        if len(prices) == 1:
            return 0

        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > m:
                m = profit
            if prices[left] > prices[right]:
                left = right
            right += 1
        return m
