# 206. ·´×ªÁ´±í
# 20190407

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        if current is None:
            return current
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
    