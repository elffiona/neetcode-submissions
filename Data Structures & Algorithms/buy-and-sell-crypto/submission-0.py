class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        cost = prices[0]

        for p in prices:
            result = max(result, p - cost)
            cost = min(cost, p)
        return result
        
        
