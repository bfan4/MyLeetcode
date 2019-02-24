class Solution:
	def letterCombinations(self, string:'str'):
		self.dict = {
						"2":"abc",
						"3":"def",
						"4":"ghi",
						"5":"jkl",
						"6":"mno",
						"7":"pqrs",
						"8":"tuv",
						"9":"wxyz"
						}
		self.res = []

		if string == '':
			return []

		self.dfs(string, 0, [])
		return self.res

	def dfs(self, string:'str', index:'int', temp:'str'):

		if len(string) == len(temp):
			self.res.append("".join (x for x in temp)
			return
		for char in self.dict[string[index]]:
			temp.append(char)
			self.dfs(string, index+1, temp)
			temp.pop()


