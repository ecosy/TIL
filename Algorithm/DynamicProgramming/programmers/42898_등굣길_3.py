# https://programmers.co.kr/learn/courses/30/lessons/42898
# 프로그래머스
# 등굣길

#%%
# tabulation을 사용한 풀이

from collections import defaultdict

def solution(m, n, puddles):
    count = 0
    dp = defaultdict(int)
    
    dp[f'1_0'] = 1
    for j in range(1, n+1):
        for i in range(1, m+1):
            
            # 장애물인 경우 방법수 0으로 초기화
            if [i, j] in puddles:
                dp[f'{i}_{j}'] = 0

            # 이전 단계의 방법수를 더하여 갱신
            else:
                dp[f'{i}_{j}'] = dp[f'{i-1}_{j}'] + dp[f'{i}_{j-1}']

    return dp[f'{m}_{n}']%1000000007