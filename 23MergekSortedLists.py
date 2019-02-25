class Solution:
	def mergeKLists(self, lists: ListNode) -> ListNode:

		self.nodes = []
		head = point = ListNode(0)

		for x in lists:
			while x:
				self.nodes.append(x.val)
				x = x.next

		for node in sorted(self.nodes):
			point.next = ListNode(node)
			point = point.next
		return head.next