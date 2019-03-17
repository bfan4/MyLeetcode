class Solution:
	def merge(self, nums1:list[int], m:int, nums2:list[int], n:int) -> None:
		nums1[:] = sorted(num1[:m] + nums2[:])