# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# leetcode #104
# 이진 트리의 최대 깊이

#%%
# 풀이 과정
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# %%
root = TreeNode(val=3,\
    left= TreeNode(val=9, left=None, right=None), 
    right= TreeNode(val=20, left= TreeNode(val=15, left= None, right= None), 
    right= TreeNode(val=7, left= None, right= None)))

#%%
import collections
# %%
queue = collections.deque([root])
len(queue)
# %%
node = queue.popleft()
node
# %%
node.left
#%%
depth = 0
while queue:
    depth += 1
    for i in range(len(queue)):
        node = queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
depth
#%%
# My Solution

import collections
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # root가 존재하지 않는 경우 예외처리
        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0
        
        # 현재 queue의 길이만큼 돌면서 
        # 같은 depth의 노드 제거, child는 queue에 추가
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth