# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        current = root

        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right

            else:
                predecessor = current.left

                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left

                else:
                    predecessor.right = None
                    result.append(current.val)
                    current = current.right

        return result
