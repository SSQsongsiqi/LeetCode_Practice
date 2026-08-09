# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = head
        tail = dummy
        while left is not None and left.next is not None:
            right = left.next
            left.next = right.next
            right.next = left
            tail.next = right
            tail = left
            left = left.next
        return dummy.next

            

        
