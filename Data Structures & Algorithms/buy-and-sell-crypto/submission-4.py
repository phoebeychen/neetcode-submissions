class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] > prices[i]:
                    profits.append(prices[j]-prices[i])
                else:
                    profits.append(0)
                    
        return max(profits)
            