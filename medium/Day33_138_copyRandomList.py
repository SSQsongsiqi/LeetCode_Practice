# 构造这个链表的 深拷贝


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None:None}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            old_to_new[current].next = old_to_new[current.next]
            old_to_new[current].random = old_to_new[current.random]
            current = current.next
        return old_to_new[head]
