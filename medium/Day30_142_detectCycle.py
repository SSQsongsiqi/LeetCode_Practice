# 给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
# 不允许修改 链表。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 集合
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()
        current = head

        while current:
            if current in visited:
                return current
                break
            visited.add(current)
            current = current.next
        return None
            
# 快慢指针
# 设slow走了s步，则f = 2s
# f比s多走了n个环的长度，即f = s + nb
# 上面两式相减，得f = 2nb ; s = nb
# 从head结点走到入环点需要走: a + nb，而slow已经走了nb，那么slow再走a步就是入环点了。如何知道slow刚好走了a步？从head开始，和slow指针一起走，相遇时刚好就是a步

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


            
            
