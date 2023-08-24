#Best time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val=0 
        min_val=float('inf') 
        for i in range(len(prices)):
            min_val=min(min_val,prices[i]) 
            max_val=max(max_val,prices[i]-min_val) 
            
        return max_val