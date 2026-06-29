class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    profit.append(prices[j]-prices[i])
                else: 
                    profit.append(0)
        return max(profit)