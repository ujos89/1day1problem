# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        reverse = head
        head = head.next
        
        while(not head):
            reverse.next = head
            head = head.next
        
        return reverse


        """
        :type head: ListNode
        :rtype: ListNode
        """