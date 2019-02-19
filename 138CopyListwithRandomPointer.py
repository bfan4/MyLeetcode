class Solution(object):
	def __init__(self):
		# 创建一个名为visitedHash的map，注意局部变量加 self
		self.visitedHash = {}

	def copyRandomList(self, head):

		#判断，如果当前节点是空，则返回空
		if head == None:
			return None

		#判断，如果当前字段在visitedHash里存在，证明已经copy过了
		if head in self.visitedHash:
			return self.visitedHash[head]

		#将当前节点head的label定义为新的node
		node = RandomListNode(head.label)

		#把他存进关键字为当前节点的map
		self.visitedHash[head] = node

		node.next = self.copyRandomList(head.next)

		node.random = self.copyRandomList(head.random)

		return node
