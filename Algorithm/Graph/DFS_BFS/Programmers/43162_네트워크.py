# https://programmers.co.kr/learn/courses/30/lessons/43162
# 프로그래머스 #43162
# 네트워크

#%%
# My Solution
from collections import defaultdict
def solution(n, computers):
    answer = 0
    
    # list to graph
    graph = defaultdict(list)
    for i in range(n):
        graph[i].append(i)
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    # leaf node까지 탐색하여 visited에 삽입
    def dfs(node, visited):
        visited.append(node)
        for _node in graph[node]:
            if _node not in visited:
                dfs(_node, visited)
        return
    
    visited = []
    for node in list(graph):
        # visited 에 있지 않은 노드만 dfs 탐색
        if node not in visited:
            answer += 1
            dfs(node, visited)

    return answer