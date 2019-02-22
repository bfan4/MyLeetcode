class Solution:
	def maxProfit(self, prices: 'list[int]') -> 'int':
		result, minPrice = 0, 2**31
		for price in prices:
			minPrice = min(minPrice, price)
			profit = price - minPrice
			result = max(result, profit)
		return result




def main():
	x = [3,4,5,8,10,4,3]
	b = Solution().maxProfit(x)
	print(b)




if __name__ == '__main__':
	main()




###########这个方法非常慢#################
# class Solution:
#     def maxProfit(self, prices: 'List[int]') -> 'int':
#         length = len(prices)
#         ans = [0]
#         for i in range(length):
#             for j in range (i+1, length):
#                 if prices[i] < prices[j]:
#                     ans.append(prices[j] - prices[i])
#                 continue
#         ret = max(ans)
#         return ret