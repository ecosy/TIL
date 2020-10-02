# https://leetcode.com/problems/assign-cookies/
# leetcode #455
# 쿠키 부여
# 그리디

# %%
# My Solution

g = [1,2,3]
s = [1,1]
#%%
import collections
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = collections.deque(sorted(s)) # 속도 최적화를 위해 데크 사용

        count = 0
        while s:
            cookie = s.popleft()

            for i in range(len(g)):
                # 쿠키보다 더 큰 아이만 있다면 break
                if cookie < g[i]: 
                    break
                # 쿠키를 줄 수 있는 아이가 있다면
                else:
                    del g[i]
                    count += 1
                    break
        return count
sol = Solution()
sol.findContentChildren(g, s)
# %%
# 책 풀이 분석 1
# 그리디 알고리즘 사용
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    child_i = cookie_j = 0
    # 만족하지 못할 때까지 그리디 진행
    while child_i < len(g) and cookie_j < len(s):
        if s[cookie_j] >= g[child_i]:
            child_i += 1
        cookie_j += 1
    return child_i

#%%
# 책 풀이 분석 2
# 이진 검색
import bisect
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    result = 0
    for _s in s:
        # 이진 검색으로 더 큰 인덱스 탐색
        # 쿠키보다 더 큰 아이의 index 탐색
        index = bisect.bisect_right(g, _s) 
        if index > result:
            result += 1
        
    return result