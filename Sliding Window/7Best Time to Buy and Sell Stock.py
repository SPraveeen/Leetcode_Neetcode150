class Solution:
    def maxProfit(self,prices:List[int]) -> int:
        buy=prices[0]
        max_profit=0
        for price in prices:
            buy=min(buy,price)
            max_profit=max(max_profit,price-buy)
        return max_profit