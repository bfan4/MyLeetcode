class Solution:
	def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'list[List[int]]':
		points.sort(key = lambda p : p[0]**2 + p[1]**2)
		return points[:K]