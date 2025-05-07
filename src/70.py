class BinaryTreeNode:
    def __init__(self, val: int = 0, left: int = 1, right: int = 2):
        self.val = val
        self.left = val + left
        self.right = val + right


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        def bf(node: BinaryTreeNode):
            if node.val == n:
                return 1
            elif node.val > n:
                return 0
            else:
                left_node = BinaryTreeNode(val=node.val + 1)
                right_node = BinaryTreeNode(val=node.val + 2)
                return bf(left_node) + bf(right_node)

        node = BinaryTreeNode()

        return bf(node)
