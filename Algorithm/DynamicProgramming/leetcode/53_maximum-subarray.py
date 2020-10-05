# https://leetcode.com/problems/maximum-subarray/
# leetcode #53
# 최대 서브 배열

#%%
nums = [-2,1,-3,4,-1,2,1,-5,4]
# %%
import collections
dp = collections.defaultdict(int)

# %%
def sub_sum(index, window):
    if dp[f'{index}_{window}']:
        return dp[f'{index}_{window}']
    
    if window == 1:
        dp[f'{index}_{window}'] = nums[index]
        return nums[index]

    dp[f'{index}_{window}'] = sub_sum(index, window - 1) + sub_sum(index + window - 1, 1)

    return dp[f'{index}_{window}']
#%%
for i in range(len(nums)):
    sub_sum(i, len(nums) - i)
dp
#%%
max(dp.values())
#%%

# My Solution
# 시간 초과 발생

import collections
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # 동적계획법의 결과를 담을 dictionary
        dp = collections.defaultdict(int)

        def sub_sum(index, window):
            # dp에 존재하는 값이면 사용
            if dp[f'{index}_{window}']:
                return dp[f'{index}_{window}']

            # window size == 1 일때 해당 index의 값 사용
            if window == 1:
                dp[f'{index}_{window}'] = nums[index]
                return nums[index]

            dp[f'{index}_{window}'] = sub_sum(index, window - 1) + sub_sum(index + window - 1, 1)

            return dp[f'{index}_{window}']

        # 모든 index, window에 대해 결과 값 계산
        for i in range(len(nums)):
            sub_sum(i, len(nums) - i)

        return max(dp.values())

#%%
# 책 풀이 분석 1
# 0 이상인 num의 수만 뒤로 더해주어 sum을 만들어 나감

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)

#%%
# 책 풀이 분석 2
# 카데인 알고리즘
# 매번 best sum을 계산하여 업데이트 시킴

import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        
        return best_sum