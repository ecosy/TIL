# https://leetcode.com/problems/permutations/
# leetcode #46

#%%

# My Solution
# Brute Force 사용
# permutation 배열이 nums 배열의 크기와 같아지기 전까지,
# dfs 로 숫자가 permutation 배열에 없는 경우 추가시킴

# 시간 복잡도 : O(N ^ (N!))
# 매번 nums의 num이 포함되어 있는지 비교하기 때문

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(permutation):
            # permutation에 모든 nums를 사용한 조합이 만들어진 경우
            if len(permutation) == len(nums):
                # 지금까지의 permutation을 정답에 더해주기
                answer.append(permutation)
                return
            # 아직 추가해야 할 nums가 있는 경우
            else:
                for num in nums:
                    # num이 permutation에 없는 경우
                    # num을 더해준 배열을 다시 재귀 호출
                    if num not in permutation:
                        temp = permutation[:]
                        temp.append(num)
                        dfs(temp)
        
        if not nums:
            return []
        
        answer = []
        dfs(permutation = [])

        return answer

#%%
s = Solution()
s.permute(nums=[1,2,3])

#%%
# 책 풀이 분석 1
# DFS 활용한 순열 생성
# 시간복잡도 : O(N!)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = [] # 순열 저장 변수

        def dfs(elements):
            # 리프 노드일 때 결과 추가
            if len(elements) == 0:
                results.append(prev_elements[:])

            # 순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                # 전달받은 elements 배열에서 원소 e 하나씩 제거
                next_elements.remove(e)

                # 순열에 원소 e 저장
                prev_elements.append(e)
                
                # e를 제거한 next_elements로 재귀 실행
                dfs(next_elements)

                # nums 개수만큼 prev_elements를 저장한 이후
                # 재귀 함수 호출이 끝나면서 nums 개수 만큼 다시 요소 삭제
                prev_elements.pop()

        dfs(nums)
        return results
#%%
s = Solution()
s.permute(nums = [1, 2, 3])
#%%
# 책 풀이 분석 2
# itertools 모듈 사용

from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list, permutations[nums]))
