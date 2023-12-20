# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        reverseHead = slow.next
        prev = None
        slow.next = None

        while reverseHead:
            temp = reverseHead.next
            reverseHead.next = prev
            prev = reverseHead
            reverseHead = temp

        first, second = head, prev

        while second:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp
