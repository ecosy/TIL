# https://programmers.co.kr/learn/courses/30/lessons/43162
# 프로그래머스 #43162
# 네트워크

#%%
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# %%
def dfs(index, visited):
    print('_______________')
    print(index, visited)
    for i, connection in enumerate(computers[index]):
        print(f'check connection : {i}, {connection}')
        if i not in visited and connection == 1:
            visited.append(i)
            print(f'add node {i}, visited : {visited}')
            dfs(i, visited)
    
#%%
visited = []
cnt = 0
# %%
# i : 0, 1, 2
for index in range(len(computers)):
    if index not in visited:
        visited.append(index)
        dfs(index, visited)
        cnt += 1
# %%
cnt
# %%
def solution(n, computers):
    def dfs(index, visited):
        for i, connection in enumerate(computers[index]):
            if i not in visited and connection == 1:
                visited.append(i)
                dfs(i, visited)
                
    visited = []
    cnt = 0 

    for index in range(len(computers)):
        if index not in visited:
            visited.append(index)
            dfs(index, visited)
            cnt += 1
    return cnt