class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)-1):
            j = i + 1
            if j <= len(prices) and prices[j] - prices[i] >= 0:
                ans += prices[j] - prices[i]
        return ans



###  Another solution   #########
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return sum([y - x for x, y in zip(prices[:-1], prices[1:]) if x < y])