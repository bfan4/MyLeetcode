class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		sortedlistNum = sorted(nums)
		if sortedlistNum[len(nums)-1] == len(nums)-1:
			return len(nums)
		for i in range(len(nums)):
			if i != sortedlistNum[i]:
				return i

########这是一个聪明的办法##############################
class Solution:
    def missingNumber(self, nums):
        return int(len(nums) * (len(nums)+1) / 2 - sum(nums))