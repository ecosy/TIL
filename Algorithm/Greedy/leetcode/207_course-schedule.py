# https://leetcode.com/problems/course-schedule/
# leetcode #207
# bfs/dfs


#%%
# 풀이 과정 

numCourses = 5
prerequisites = [[4,1], [1,0], [1,3], [3,2], [2,1]]

#%%
# list to dict
import collections
graph = collections.defaultdict(list)

for end, start in prerequisites:
    graph[start].append(end)
graph
# %%
def dfs(node, visited):

    if node in visited:
        return False
    
    if not graph[node]:
        return True
    
    print('node : ', node)

    visited.append(node)
    print('visited : ', visited)

    print('graph ', graph)
    for v in graph[node]:
        print('v : ', v)
        if not dfs(v, visited):
            return False
        print('visited : ', visited)
        print('____________________________')
    visited.pop()
    return True

# %%
for k in list(graph):
    print('k : ', k)
    if not dfs(k, []):
        print('false')
        break
print('True')

#%%

# My Solution
# 시간 초과 발생!

import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # list to dict
        graph = collections.defaultdict(list)

        for end, start in prerequisites:
            graph[start].append(end)
        
        # 순환구조가 발생하면 False 리턴
        def dfs(node, visited):
            
            # 중복 방문 여부 확인
            if node in visited:
                return False

            visited.append(node)

            for v in graph[node]:
                if not dfs(v, visited):
                    return False
            visited.pop()
            return True
        
        # graph의 Key로 탐색 시작
        for k in list(graph):
            if not dfs(k, []):
                return False
        return True      
# %%

# 책 풀이 분석 1
# DFS로 순환 구조 판별

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()

    def dfs(i):
        # 순환구조이면 False
        if i in traced:
            return False
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        return True

    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    
    return True
# %%

# 책 풀이 분석 2
# 가지치기를 이용한 최적화

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)
    # 그래프 구성
    for x, y in prerequisites:
        graph[x].append(y)
    
    traced = set()
    visited = set()

    def dfs(i):
        # 순환 구조이면 False
        if i in traced:
            return False
        # 이미 방문했던 노드이면 False
        if i in visited:
            return True
        
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        # 탐색 종료 후 순환 노드 삭제
        traced.remove(i)
        # 탐색 종료 후 방문 노드 추가
        visited.add(i)

        return True
    
    # 순환 구조 판별
    for x in list(graph):
        if not dfs(x):
            return False
    return True