# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# leetcode >> Tree >> 104
# maximum depth of binary tree

#%%
# Definition for a binary tree node.
import collections

# leetcode 입력이 Treenode instance 변수로 주어짐
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        # 입력 tree가 존재하지 않는 경우
        if root is None:
            return 0

        queue = collections.deque([root])
        depth = 0

        while queue:
            # bfs 반복 횟수 == depth
            depth += 1

            # (bfs) 같은 depth의 node를 queue에서 추출하여, 
            # child를 queue에 삽입
            for _ in range(len(queue)):
                current_node = queue.popleft()
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)

        return depth