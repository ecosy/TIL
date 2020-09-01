# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# leetcode >> tree
# convert-sorted-array-to-binary-search-tree

#%%
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        # Left Node인 경우, 혹은 입력이 없는 경우 예외처리
        if not nums:
            return None

        # 중앙값 index 추출
        mid = len(nums) // 2

        # 중앙값에 해당하는 TreeNode instance 생성
        node = TreeNode(val=nums[mid])
        node.left = self.sortedArrayToBST(nums=nums[:mid])
        node.right = self.sortedArrayToBST(nums=nums[mid+1:])

        return node
# %%
S = Solution()
S.sortedArrayToBST(nums=[-10,-3,0,5,9])
