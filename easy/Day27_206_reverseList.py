# 反转链表

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next   # 先保存下一个节点
            current.next = prev        # 当前节点反向指向前一个节点
            prev = current             # prev向后移动
            current = next_node        # current向后移动

        return prev
