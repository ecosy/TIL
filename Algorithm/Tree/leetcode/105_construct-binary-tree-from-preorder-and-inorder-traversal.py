# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# leetcode >> tree
# construct-binary-tree-from-preorder-and-inorder-traversal

######################################################################################

# Solution 

#%%
preorder = [3,9, 10, 20,15,7]
inorder = [10, 9,3,15,20,7]

# %%
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            root_index = inorder.index(preorder.pop(0))
        
            node = TreeNode(inorder[root_index])
            node.left = self.buildTree(preorder, inorder[:root_index])
            node.right = self.buildTree(preorder, inorder[root_index+1:])

            return node

#%%
######################################################################################

# Solving Process

#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#%%
root = preorder.pop(0)

inorder_root_index = -1
for i in range(len(inorder)):
    if inorder[i] == root:
        inorder_root_index = i
        break
inorder_root_index

#%%
li = [1, 2, 3]
li.index(-1)

#%%
from typing import List
def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

    if inorder :
        root = TreeNode(val=preorder.pop(0))

        # inorder_root_index = inorder.index(root)
        inorder_root_index = -1
        for i in range(len(inorder)):
            if inorder[i] == root:
                inorder_root_index = i
                break
            
        root.left = buildTree(preorder, inorder_root_index=inorder[:inorder_root_index])
        root.right = buildTree(preorder, inorder= inorder[inorder_root_index+1:])

        return root