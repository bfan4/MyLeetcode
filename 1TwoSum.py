class solution:
	def twoSum(self, nums, target):
		memory = {}
		for i in range(len(nums)):
			if num[i] in memory:
				return [memory[num[i]], i]
			else:
				memory[target - num[i]] = i

		







class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        memory = {}
        for i in range(len(nums)):
            if nums[i] in memory:
                return [memory[nums[i]], i]
            else:
                memory[target - nums[i]] = i