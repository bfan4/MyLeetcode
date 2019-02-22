class Solution:
	def isPalindrome(self, x:'int'):
		num = str(x)
		length = len(num)
		for i in range(0,length):
			j = -1-i
			if num[i] == num[j]and i <= length-j:
				continue
			elif num[i] == num[j] and i >length-j:
				return True
			elif num[i] != num[j]:
				return False
		return True









def main():
	x = 10000021
	b = Solution().isPalindrome(x)
	print(b)




if __name__ == '__main__':
	main()
