class Solution:
	def coinChange(self, coins, amount):
		#构建一个amount+1 个元素的数组，每个元素的值是amount+1，其实只要是比amount大就可以
		dp = [amount+1] * (amount +1)
		#第0位置为0，因为找回0元需要0个硬币
		dp[0] = 0
		#从数组dp的第一个开始遍历
		for i in range(1, amount+1):
			#c中存着硬币面值，遍历一遍
			for c in coins:
				#i其实就是要找回的零钱数，i>=c其实就是说明可以找回，否则零钱面值过大无法找钱
				if i >= c:
					#判断，也是动态编程的核心部分
					dp[i] = min(dp[i], dp[i-c]+1)
		if dp[amount] == amount + 1:
			return -1
		return dp[amount]


# class Solution(object):
# 	def coinChange(self, coins, amount):
# 		"""
#         :type coins: List[int]
#         :type amount: int
#         :rtype: int
#         """
# 		rs = [amount+1] * (amount+1)
# 		rs[0] = 0
# 		for i in range(1, amount+1):
# 			for c in coins:
# 				if i >= c:
# 					rs[i] = min(rs[i], rs[i-c] + 1)

# 		if rs[amount] == amount+1:
# 			return -1
# 		return rs[amount]




def main():
			coins = [5,1,2]
			amount = 11;

			ret = Solution().coinChange(coins, amount)

			out = str(ret);
			print(out)
		
if __name__ == '__main__':
	main()