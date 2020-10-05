# https://leetcode.com/problems/fibonacci-number/
# leetcode #509
# 피보나치 수

#%%
# My Solution 1
# bottom up
# tabulation
#%%
import collections
def fib(n):
    fib_num = collections.defaultdict(int)
    fib_num[0] = 0
    fib_num[1] = 1

    for i in range(2, n  + 1):
        fib_num[i] = fib_num[i - 1] + fib_num[i - 2]

    return fib_num[n]
fib(4)
# %%
# My Solution 2
# top down
# memorization
fib_num = {}
def fib(n):
    if n <= 1:
        return n

    if n in fib_num:
        return fib_num[n]

    fib_num[n] = fib(n - 1) + fib(n - 2)

    return fib_num[n]
fib(5)
#%%
# 책 풀이 분석 1
# 재귀 구조 브루트 포스

class Solution:    
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)

#%%
# 책 풀이 분석 2
# Memorization

import collections
class Solution:
    # default value = 0 
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N

        # 저장되어 있는 계산 값 사용        
        if self.dp[N]:
            return self.dp[N]

        self.dp[N] = self.fib(N - 1) + self.fib(N - 2)
        return self.dp[N]

#%%
# 책 풀이 분석 3
# Tabulation

import collections
class Solution:
    dp = collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[1] = 1

        # 재귀를 사용하지 않고 반복으로 풀이
        # 작은 값부터 직접 계산하면서 타뷸레이션 
        for i in range(2, N + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]
        return self.dp[N]

#%%
# 책 풀이 분석 4
# 두 변수만 이용해 공간 절약

# 공간 복잡도 : O(1)
# 시간 복잡도 : O(n)

class Solution:
    def fib(self, N: int) -> int:
        x, y = 0, 1

        for i in range(0, N):
            x, y = y, x + y
        return x

#%%
# 책 풀이 분석 5
# 행렬

# 시간복잡도 : O(log n)
# 선형대수에서 행렬의 n 승을 계산하는 방식
# numpy 모듈 사용 -> leetcode에서는 동작 안함

import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        M = np.matrix([0, 1], [1, 1])
        vec = np.array([[0], [1]])

        return np.matnul(M ** n, vec)[0]