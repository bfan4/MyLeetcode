height = [1,8,6,2,5,4,8,3,7]

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0; j= len(height)-1
        maxV = 0

        while i != j :
	
            if height[i] < height[j]:
                sq = height[i] * (j-i)
                i += 1
            else:
                sq = height[j] * (j-i)
                j -= 1
            maxV = max(maxV, sq)
        return maxV


class Solution:
    def maxArea(self, height: List[int]) -> int:        
        i = 0; j= len(height)-1
        maxV = 0
        while i != j :
            if height[i] < height[j]:
                maxV = max((height[i] * (j-i)), maxV)
                i += 1
            else:
                maxV = max((height[j] * (j-i)), maxV)
                j -= 1
        return maxV





















##这个办法对于数据比较少的时候可以使用，对于大数据不适用###########
# class Solution:
# 	def maxArea(self, height: List[int]) -> int:
# 		maxV = 0
# 		length = len(height)
# 		for i in range(length):
# 			for j in range(i+1, length):
# 				maxV = max(maxV, min(height[i], height[j])*abs(i-j))
# 		return maxV