class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_day = -1
        sell_day = -1
        profit = 0
        i = 0
        j = i + 1
        while i < len(prices) and j < len(prices):
            cur_profit = prices[j] - prices[i]
            if cur_profit > profit:
                profit = cur_profit
                buy_day = i
                sell_day = j
                j = j + 1
            elif cur_profit <= 0:
                i = j
                j = i + 1
            else : 
                j = j + 1
        return profit
            
            

        