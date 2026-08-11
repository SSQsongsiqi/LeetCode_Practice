# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 只有0个或1个节点，直接返回
        if not head or not head.next:
            return head

        # 1. 找中点
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 从中间断开
        right = slow.next
        slow.next = None

        # 3. 分别排序左右两边
        left = self.sortList(head)
        right = self.sortList(right)

        # 4. 合并两个有序链表
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # 有一边可能还有剩余
        current.next = left if left else right

        return dummy.next
