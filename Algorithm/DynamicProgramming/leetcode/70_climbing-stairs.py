# https://leetcode.com/problems/climbing-stairs/
# leetcode #70
# 계단 오르기

#%%
n = 5
# %%
import collections
fib_dp = collections.defaultdict(int)

def fib(n):
    if n <= 1:
        return n

    if fib_dp[n]:
        return fib_dp[n]

    fib_dp[n] = fib(n - 1) + fib(n - 2)

    return fib_dp[n]
# %%
fib(5)
#%%
def climbStairs(n):
    if n == 1:
        return 1
    return climbStairs(n - 1) + fib(n - 1)
# %%
climbStairs(38)

#%%

# My Solution

import collections
class Solution:
    # 피보나치 수를 저장하기 위한 dictionary
    fib_dp = collections.defaultdict(int)

    # 피보나치 수를 계산, 리턴
    def fib(self, n):
        if n <= 1:
            return n
        if self.fib_dp[n]:
            return self.fib_dp[n]
        self.fib_dp[n] = self.fib(n - 1) + self.fib(n - 2)

        return self.fib(n - 1) + self.fib(n - 2)

    # n에 맞는 경우의 수 리턴
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        return self.climbStairs(n - 1) + self.fib(n - 1)

#%%
# 책 풀이 분석 1
# 재귀 구조 브루트 포스

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# %%
# 책 풀이 분석 2
# Memorization

import collections
class Solution:
    dp = collections.defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return 2
        
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
