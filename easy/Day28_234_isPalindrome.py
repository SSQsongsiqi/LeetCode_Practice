# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 法一
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        current = head

        while current is not None:
            nums.append(current.val)
            current = current.next

        return nums == nums[::-1]


# 法二：快慢指针＋反转后半部分
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # 1. 找到链表中点
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # 2. 反转后半部分链表
        prev = None
        current = slow

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # 3. 比较前半部分和后半部分
        left = head
        right = prev

        while right is not None:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True
