"""
https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1

        if root.left == None or root.right == None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


class _Solution1:
    """
    深度优先搜索
    输入：root = [2,null,3,null,4,null,5,null,6]
    输出：5
    实际输出 2 由于将null空节点层也输出了
    """

    def minDepth(self, root: TreeNode) -> int:

        return self._minDepth(root, depth=1)

    def _minDepth(self, node, depth):
        if not node:
            return 0
        if not node.left and not node.right:
            return depth
        if node.left:
            leftDepth = self._minDepth(node.left, depth + 1)
        else:
            leftDepth = depth
        if node.right:
            rightDepth = self._minDepth(node.right, depth + 1)
        else:
            rightDepth = depth
        return min(leftDepth, rightDepth)


class _Solution1_1:
    """
    深度优先搜索
    输入：root = [2,null,3,null,4,null,5,null,6]
    输出：5
    实际输出 2 判断条件顺序错误
    """

    def minDepth(self, root: TreeNode) -> int:

        return self._minDepth(root, depth=1)

    def _minDepth(self, node, depth):
        if not node:
            return 0
        if not node.left and not node.right:
            return depth
        if node.left or node.right:
            leftDepth = self._minDepth(node.left, depth + 1)
            rightDepth = self._minDepth(node.right, depth + 1)
            return max(leftDepth, rightDepth)
        if node.left and node.right:
            leftDepth = self._minDepth(node.left, depth + 1)
            rightDepth = self._minDepth(node.right, depth + 1)
            return min(leftDepth, rightDepth)


class Solution1_2:
    """
    深度优先搜索
    输入：root = [2,null,3,null,4,null,5,null,6]
    输出：5, 正确答案
    """

    def minDepth(self, root: TreeNode) -> int:

        return self._minDepth(root, depth=1)

    def _minDepth(self, node, depth):
        if not node:
            return 0
        if not node.left and not node.right:
            return depth
        if node.left and node.right:  # 这条必须在后边判断条件的前边
            leftDepth = self._minDepth(node.left, depth + 1)
            rightDepth = self._minDepth(node.right, depth + 1)
            return min(leftDepth, rightDepth)
        if node.left or node.right:
            leftDepth = self._minDepth(node.left, depth + 1)
            rightDepth = self._minDepth(node.right, depth + 1)
            return max(leftDepth, rightDepth)


class Solution2:
    """
    广度优先搜索，超出时间限制
    """

    def minDepth(self, root: TreeNode) -> int:
        depth = 0
        if not root:
            return 0
        queue = [root]
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.pop(0)
                if not node.left and not node.right:
                    return depth
                # if node.left and node.right:  # 这里的判断冗余，而且导致超时，因为多次append，如果非要这么写，需要在后边限制node必须缺一个孩子
                #     queue.append(node.left)
                #     queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)


from collections import deque


class Solution3:
    """

    """

    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0
        que = deque([(root, 1)])  # 需要注意格式
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
