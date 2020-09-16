# https://leetcode.com/problems/combinations/
# leetcode #77


#%%
n = 4
k = 2
# %%
answer = []
nums = [i+1 for i in range(4)]
nums
#%%
def dfs(nums, combination):
    if len(combination) == k:
        answer.append(combination)
        return

    else:
        for i in range(len(nums)):
            next_nums = nums[i+1:]

            next_combination = combination[:]
            next_combination.append(nums[i])
            dfs(next_nums, next_combination)          
#%%
dfs(nums=nums, combination=[])
answer
# %%

# My Solution
# dfs 재귀 호출을 할때
# 남아있는 숫자열 nums의 숫자를 하나씩 빼면서 넘겨서
# 다음 번 호출에서 남아있는 숫자열에 대해 조합을 만들게 함

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        nums = [i+1 for i in range(n)]

        def dfs(nums, combination):
            # 조합의 크기가 k개일 때 종료
            if len(combination) == k:
                answer.append(combination)
                return

            # 조합이 크기가 k보다 작을 때
            else:
                for i in range(len(nums)):
                    # 다음 재귀함수에 넘길 nums는 숫자를 하나 줄임
                    next_nums = nums[i+1:]

                    # nums의 숫자를 조합 변수에 하나씩 저장
                    next_combination = combination[:]
                    next_combination.append(nums[i])
                    
                    # 다음 단계를 위한 재귀 호출
                    dfs(next_nums, next_combination)          
        dfs(nums=nums, combination=[])
        return answer

#%%

# 책 풀이 분석 1
# DFS로 K개 조합 생성

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
            
            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                # (i ~ n)까지 돌면서 elements의 추가되고
                # k - 1 번째에는 그 다음의 i+1 수부터 추가됨 
                dfs(elements, start = i + 1, k = k - 1)
                elements.pop()

        dfs([], 1, k)
        return results

#%%

# 책 풀이 분석 2
# itertools 모듈 사용

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n + 1), k))