# https://leetcode.com/problems/merge-two-binary-trees/
# leetcode #617
# 두 이진 트리 병합

#%%
# 책 풀이 분석
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)

            return node
        else:
            print(t1 or t2)
            return t1 or t2