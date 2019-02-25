class Solution:
    def reverseList(self, head):
        prev = None
        cur = head
        
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev



class Solution:
	def reverseList(self, prev = None, head):
		if head == None:
			return prev
		next = head.next
		head.next = prev
		return everseList(head, next)