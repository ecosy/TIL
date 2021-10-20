#%%
# https://softeer.ai/practice/info.do?eventIdx=1&psProblemId=390

#%%
# N = 5
N = 8
# A = [3, 2, 1, 4, 5]
A = [1, 3, 2, 1, 3, 4, 5, 2]

#%%
N = 1 
A = [1]

#%%
N = 5 
A = [5,4,3,2,1]

#%%
dp = dict() # {index : max count of index}
#%%
def dfs(index, count):

    # DP Mem 검사
    # index의 돌을 처음 밟은 경우
    if index not in dp:
        dp[index] = count
    
    # 이전에 저장된 최대 개수 갱신
    else:
        # count가 더 큰 경우, 갱신
        if dp[index] < count : 
            dp[index] = count
        # 더 작은 경우, 종료
        else:
            return
         
    # 앞의 더 작은 수로 이동
    for i in range(index-1, -1, -1):
        # 앞의 수가 더 작은 경우, 이동
        if A[i] < A[index]:
            dfs(i, count+1)

    return

#%%
for i in range (N-1, -1, -1):
    dfs(i, 1)
#%%
dp
#%%
print(max(dp.values()))

#%%
#######################################
######### solution 
#######################################

#%%
import sys
sys.setrecursionlimit(3*pow(10,3))

N = int(input())

A = list(map(int, input().split()))

dp = dict() # {index : max count of index}

def dfs(index, count):
    global dp, A
    # DP Mem 검사
    # index의 돌을 처음 밟은 경우
    if index not in dp:
        dp[index] = count
    
    # 이전에 저장된 최대 개수 갱신
    else:
        # count가 더 큰 경우, 갱신
        if dp[index] < count : 
            dp[index] = count
        # 더 작은 경우, 종료
        else:
            return
         
    # 앞의 더 작은 수로 이동
    for i in range(index-1, -1, -1):
        # 앞의 수가 더 작은 경우, 이동
        if A[i] < A[index]:
            dfs(i, count+1)
    return


for i in range (N-1, -1, -1):
    dfs(i, 1)

print(max(dp.values()))
