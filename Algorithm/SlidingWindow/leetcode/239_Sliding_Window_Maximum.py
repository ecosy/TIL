# https://leetcode.com/problems/sliding-window-maximum/

#%%
nums = [1,3,-1,-3,5,3,6,7]
k = 3

#%%
start_window = 0
end_window = start_window + k

#%%
max(nums)
#%%
max(nums[start_window : end_window])

#%%
answer = []
while end_window <= len(nums):
    answer.append(max(nums[start_window : end_window]))
    start_window += 1
    end_window += 1
answer
# %%
# My Solution

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return nums 
            
        answer = []
        start_window = 0
        end_window = start_window + k

        # nums 배열의 start_window 인덱스 ~ end_window 인덱스 중 max를 추출
        # Brute Force 방식으로 각 윈도우 구간의 max를 구함
        while end_window <= len(nums):
            answer.append(max(nums[start_window : end_window]))
            start_window += 1
            end_window += 1
        return answer

#%%
# 책 풀이 #1
# >> 브루트 포스로 계산

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums 배열이 비어있는 경우, 예외처리
        if not nums:
            return nums
        
        # 인덱스를 저장하는 변수를 따로 선언하지 않고,
        # index 0 ~ (len(nums) - k + 1) 까지 순회하며 탐색함
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))
        return k
#%%
# 책 풀이 #2
# >> 큐 이용한 최적화

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        results = []
        window = collections.deque() # 최적화를 위해 데크 사용
        current_max = float('-inf') # 최솟값 대입
        
        for i, v in enumerate(nums):
            window.append(v)

            # 초반 window 내에 v가 k개가 될 때까지 삽입
            if i < k - 1:
                continue

            # 최댓값이 초기화된 경우에만 window max 계산
            if current_max == float('-inf'):
                current_max = max(window)

            # 새로 추가된 값이 기존 최댓값보다 큰 경우 교체
            elif v > current_max:
                current_max = v
            
            results.append(current_max)

            # 최댓값이 윈도우에서 빠지면 초기화
            if current_max == window.popleft(): # -> 변수를 따로 선언하지 않고, 최적화시킨 표현!
                current_max = float('-inf')
        
        return results
#%%

# 다시 풀어본 나의 풀이

import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if now nums:
            return nums

        results = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):

            window.append(v)

            if i < k - 1:
                continue
            
            # max값이 초기화 되었다면, 현재 window의 max값 갱신
            if current_max == float('-inf'):
                current_max = max(window)
            
            # 현재 v값이 max값보다 크다면, max값 갱신
            elif v > current_max:
                current_max = v

            results.append(current_max)

            # 최댓값이 큐에서 빠지게 되면, -inf로 max값 초기화
            if current_max == window.popleft():
                current_max = float('-inf')
        
        return results