# https://leetcode.com/problems/subsets/
# leetcode # 78

#%%
nums = [1,2,3]
#%%
answer = []
#%%
def dfs(combination, index, k):

    if index > len(nums):
        return

    elif len(combination) == k:
        answer.append(combination[:])
        return

    for num in nums[index:]:
        combination.append(num)
        dfs(combination, nums.index(num) + 1, k)
        combination.pop() 
#%%
for i in range(len(nums)+1):
    dfs(combination = [], index = 0, k = i)
answer
# %%

# My Solution

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(combination, index, k):
            if index > len(nums):
                return

            elif len(combination) == k:
                answer.append(combination[:])
                return

            for num in nums[index:]:
                combination.append(num)
                dfs(combination, nums.index(num) + 1, k)
                combination.pop() 

        answer = []        
        for i in range(len(nums)+1):
            dfs(combination = [], index = 0, k = i)

        return answer

#%%

# 책 풀이 분석

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            # 매번 결과 추가
            result.append(path)

            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]]) 
        
        dfs(0, [])
        return result