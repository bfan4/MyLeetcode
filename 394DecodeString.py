class Solution:
	def decodeString(self, s):
		stack = []
		curNum = 0
		curString = ""
		prevString = ''
		for char in s:
			if char.isdigit():
				curNum = curNum * 10 + int(char)
			elif char == '[':
				stack.append(curString)
				stack.append(curNum)
				curString = ""
				curNum = 0
			elif char == ']':
				num = stack.pop()
				prevString = stack.pop()
				curString = prevString + num * curString
			else:
				curString += char
		return curString
