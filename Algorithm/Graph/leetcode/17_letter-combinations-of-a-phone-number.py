# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# leetcode # 17

#%%

# 책의 풀이 분석

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # 끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return
            
            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                # 숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        # 예외 처리
        if not digits:
            return []

        dic = {
            "2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
            "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"
        }
        result = []
        dfs(index = 0, path = "")

        return result 

#%%
s = Solution()
s.letterCombinations("2345")

#%%

# leetcode solution

# Time Complexity : O(3^N * 4^M)
# N : 3개짜리 문자를 가진 숫자의 개수
# M : 4개짜리 문자를 가진 숫자의 개수

# Space Complexity : O(3^N * 4^M)
# 정답을 저장할 공간이 조합 수 만큼 필요함

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # 더 이상 조합할 숫자가 없다면
            if len(next_digits) == 0:
                # 정답에 지금까지 완성한 조합 더하기
                output.append(combination)

            # 더 조합할 숫자가 있다면
            else:
                # 다음에 조합할 숫자의 알파벳 각각을
                # 지금까지의 조합에 더하기
                for letter in phone[next_digits[0]]:
                    # 조합한 문자와, 남은 숫자 배열로 재귀 실행
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output