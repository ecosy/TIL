# https://leetcode.com/problems/combination-sum/
# leetcode # 39

#%%
candidates = [2,3,6,7]
target = 7
# %%
answer = []
#%%
def dfs(index, combination):
    if sum(combination) > target:
        return

    elif sum(combination) == target:
        answer.append(combination[:])
        return
    
    for num in candidates[index:]:
        if sum(combination) + num > target:
            break
        combination.append(num)
        dfs(candidates.index(num), combination)
        combination.pop()
# %%
dfs(index = 0, combination = [])
answer
#%%

# My Solution

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, combination):
            # combination의 합이 target과 같은 경우,
            # combination의 복사본을 정답에 저장
            if sum(combination) == target:
                answer.append(combination[:])
                return

            # index 번째 숫자부터 combination에 추가
            for num in candidates[index:]:
                # 새로운 수를 더한 합이 target보다 큰 경우 가지치기
                if sum(combination) + num > target:
                    break
                # 새로운 수를 combination에 추가
                combination.append(num)
                # 추가한 수의 index부터 재귀함수로 탐색
                dfs(candidates.index(num), combination)
                # 재귀 호출 후 추가한 수 제거
                combination.pop()

        if not candidates:
            return []

        answer = []
        # 가지치기를 위해 미리 정렬
        candidates.sort()

        dfs(index = 0, combination = [])
        return answer
#%%

# 책 풀이 분석

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum, index, path):
            # 종료 조건
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            # 자신부터 하위 원소까지의 나열 재귀 호출
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
            
        dfs(csum = target, index = 0, path = [])
        return result