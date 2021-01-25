# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        answer = None

        while(head):
            tmp = head
            head = head.next
            tmp.next = answer
            answer = tmp
            
        return answer
        