"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
	def connect(self, root):
		if root == None:
			return 
		if not root.left and not root.right :
			root.next = None
		queue =  collections.deque([(root, 1)])
		dic = collections.defaultdict(list)
		while queue:
			node, level = queue.popleft()
			if not node:
				continue
			dic[level].append(node)

			if node.left:
				queue.append((node.left, level + 1))
			if node.right:
				queue.append((node.right, level + 1))

		for levels , nodes in dic.items():
			i = 0
			while i < len(nodes) - 1:
				nodes[i].next = nodes[i+1]
				i += 1
			nodes[i].next = None
		return root
