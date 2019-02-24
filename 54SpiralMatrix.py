class Solution:
	def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
		i = 0
		j = 0
		istart = 0
		jstart = 0
		ileng = len(matrix)
		jleng = len(matrix[0])
		ans = []
		totle = ileng * jleng 
		while totle >= 0:
			####      >       ####
			if i == 0 and j == 0:
				for j in range(jstart, jleng):
					ans.append(matrix[i][j])
					totle -= 1
				istart += 1
				j = jleng
				i = 0
			####      V       ####
			elif i == 0 and j == jleng:
				for i in range(istart, ileng):
					ans.append(matrix[i][j])
					totle -= 1
				jleng -= 1
				j = jleng 
				i = ileng
			####       <       ####
			elif i == ileng and j == 0:
				for j in range(jleng,jstart):
					ans.append(matrix[i][j])
					totle -= 1
				ileng -= 1
				j = 0
				i = ileng
			elif i == ileng and j == 0:
				for i in range(ileng, istart):
					ans.append(matrix[i][j])
					totle -= 1
				jstart -= 1
				j == 0
				i == 0
			return ans
