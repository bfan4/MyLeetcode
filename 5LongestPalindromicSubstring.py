class Solution:
	def longestPalindrome(self, s: str) -> str:
		longest = ''
		for i in range(len(s)):
			temp = self.tool(i,i,s)
			if len(longest) < len(temp):
				longest = temp
			
			temp = self.tool(i, i+1, s)
			if len(longest) < len(temp):
				longest = temp
		return longest

	def tool(self, left, right, s):
		while right < len(s) and left >=0 and s[right] == s[left]:
			right += 1
			left -=1
		return s[left+1:right]
