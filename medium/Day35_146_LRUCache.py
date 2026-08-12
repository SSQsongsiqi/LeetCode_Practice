# LRU缓存

'''
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.capacity = capacity

        # key -> Node
        self.cache = {}

        # 两个虚拟节点
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left


    # 从链表中删除 node
    def remove(self, node):

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


    # 把 node 放到最右边
    # 最右边表示最近使用
    def insert(self, node):

        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 刚使用过，所以移动到最右边
        self.remove(node)
        self.insert(node)

        return node.value


    def put(self, key: int, value: int) -> None:

        # 如果已经存在，先删旧节点
        if key in self.cache:
            self.remove(self.cache[key])

        # 创建新节点
        node = Node(key, value)

        # 放入字典
        self.cache[key] = node

        # 放到链表最右边
        self.insert(node)

        # 超出容量
        if len(self.cache) > self.capacity:

            # 最左边是真正最久没使用的节点
            lru = self.left.next

            self.remove(lru)

            # 字典也必须删除
            del self.cache[lru.key]
