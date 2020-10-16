# https://leetcode.com/problems/invert-binary-tree/
# leetcode #226
# 이진 트리 반전

#%%
# 책 풀이 분석 1
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = \
                self.invertTree(root.right), self.invertTree(root.left)
        return None

#%%
# 책 풀이 분석 2
# 반복 구조 BFS
# Top Down
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()
            # 부모 노드부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                queue.append(node.left)
                queue.append(node.right)
        return root

#%%
# 책 풀이 분석 3
# 반복 구조 DFS
# Bottom Up
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left

                stack.append(node.left)
                stack.append(node.right)
        return root

#%%
# 책 풀이 분석 4
# 반복 구조로 DFS 후위 순회
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = collections.deque([root])

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)

                node.left, node.right = node.right, node.left
        return root