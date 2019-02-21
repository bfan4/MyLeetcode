class Solution(object):
	def isHappy(self, n:'int') -> 'bool':
		mem = set()
		while n != 1:
			mem.add(n)
			n = sum(int(i) ** 2 for i in str(n))   
			if n == 1 or n == 7:
				return True
			elif n in mem:
				return False
		return True

def main():
	n = 124
	ret = Solution().isHappy(n)

	print(ret)



if __name__ == '__main__':
	main()














'''
class Solution(object):
	def isHappy(self, n:'int') -> 'bool':
		mem = set()
		while n != 1:
			n = sum([int(i) ** 2 for i in str(n)])
			if n in mem:
				return False
			else:
				mem.add(n)
		return True
'''




