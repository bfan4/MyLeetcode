# 141. Linked List Cycle
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
            