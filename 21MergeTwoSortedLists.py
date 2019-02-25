class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        start = None

        if l1.val < l2.val:
            start = l1 
            start.next = self.mergeTwoLists(l1.next, l2)
        else:
            start = l2
            start.next = self.mergeTwoLists(l1, l2.next)
        return start
































def main():
	s = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
	ret = Solution().numUniqueEmails(s)
	out = (ret);
	print(out)

if __name__ == '__main__':
	main()