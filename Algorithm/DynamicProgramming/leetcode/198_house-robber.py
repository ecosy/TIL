# https://leetcode.com/problems/house-robber/
# leetcode #198
# 집 도둑

#%%
# 책 풀이 분석 1
# 재귀 구조 브루트 포스

class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(i: int) -> int:
            if i < 0:
                return 0
            return max(_rob(i - 1), _rob(i - 2) + nums[i])
        return _rob(len(nums) - 1)

#%%
# 책 풀이 분석 2
# Tabulation 
# dp [i] : i번째 까지의 집 중에서 최댓값
# dp [i] => dp[i - 1] (i번째 수를 건너뛴 경우), 
#           dp[i - 2] + nums[i] : 2번째 이전 max 값과 i번째 수를 더한 값
#           이 중 더 큰 값으로 갱신

import collections
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 예외 처리
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp.popitem()[1]