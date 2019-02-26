class Solution:
	def numJewelsInStones(self, J: str, S: str) -> int:
		return sum(map(J.count, S))


##########这里最牛逼的是map()的妙用，map（function， data）
##########fction定义一种计算规则，data里的数据按照计算规则计算