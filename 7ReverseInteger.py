class Solution:
	def reverse(self, x: 'int') -> 'int':
		num = str(x)
		sign = False
		ans = 0
		ret = ''
		if num[0] == '-':
			num = num[1:]
			sign = True
		ret = num[::-1]
		ans = int(ret)
		if sign:
			ans *= -1
		if ans not in range(-2**31, 2**31):
			return 0
		else:return ans
		return ans





def main():
	x = -123123143434
	b = Solution().reverse(x)
	print(b)




if __name__ == '__main__':
	main()
