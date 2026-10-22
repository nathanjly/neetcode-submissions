class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0
        left, right = 0, 1
        profit = 0
        while (right < length):
            if prices[left] < prices[right]:
                profit = max(prices[right] - prices[left], profit)
            else:
                left = right
            right += 1

        return profit