class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = left +1
        maxp = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                maxp = max([maxp,prices[right] - prices[left]])
            else:
                left = right
            right = right + 1
        return maxp

