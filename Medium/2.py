# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = res = ListNode(0)
        while l1 or l2 or carry:
            x = y = 0
            
            if l1:
                x = l1.val
                l1 = l1.next
            if l2:
                y = l2.val
                l2 = l2.next
                
            carry, num = divmod(x + y + carry, 10)
            res.next = ListNode(num)
            res = res.next
        
        return root.next