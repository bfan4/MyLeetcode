from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        self.ans = []
        for s in cpdomains:
            num, addr = s.split(' ')
            addr = addr.split('.')
            while len(addr)>0:
                web = '.'.join(addr)
                
                dic[web] += int(num)
                addr = addr[1:]
        for web, count in dic.items():
            self.ans.append(str(count)+" "+web)
        return self.ans
















def main():
	
	ret = Solution().subdomainVisits(n)

	print(ret)



if __name__ == '__main__':
	main()