# https://leetcode.com/problems/reconstruct-itinerary/
# leetcode #332
# 일정 재구성
# graph

#%%
# tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets = [["JFK","NUL"],["JFK","KRT"],["KRT","JFK"]]
# %%

# My Solution #1
# testcase 통과 못했음
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# -> 탐색이 아니라, 알파벳 역순 우선으로 탐색하기 때문

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # List to Dict
        graph = defaultdict(list)

        # tickets list to dictionary
        for start, end in tickets:
            graph[start].append(end)
        
        # graph value를 역순 정렬
        for key, _ in graph.items():
            graph[key].sort(reverse=True)
        
        # JFK부터 연결된 graph에서 알파벳 역순으로 탐색
        start = 'JFK'
        answer = [start]
        while len(answer) <= len(tickets):
            if not graph[start]:
                break

            start = graph[start].pop()
            answer.append(start)
        return answer
#%%
# 책 풀이 분석 1
# DFS로 일정 그래프 구성
import collections
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    # 그래프 알파벳 순서대로 구성 
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route = []
    def dfs(node):
        # 첫 번째 값을 읽어 어휘 순 방문
        while graph[node]:
            dfs(graph[node].pop(0))
        route.append(node)
    
    dfs('JFK')

    # 다시 뒤집어 어휘 순 결과 리턴
    return route[::-1]

# %%
# 책 풀이 분석 2
# 스택 연산으로 큐 연산 최적화 시도

def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프를 뒤집어서 구성
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)
    
    route = []
    def dfs(a):
        # 마지막 값을 읽어 어휘 순 방문
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    
    dfs('JFK')
    # 다시 뒤집어 어휘 순 결과 리턴
    return route[::-1]

#%%
# 책 풀이 분석 3
# 일정 그래프 반복
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    
    route, stack = [], ['JFK']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        route.append(stack.pop())
    
    # 다시 뒤집어 어휘 순 결과 리턴
    return route[::-1]
