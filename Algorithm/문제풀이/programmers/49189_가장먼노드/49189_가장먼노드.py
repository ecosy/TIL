#%%
# https://programmers.co.kr/learn/courses/30/lessons/49189

#%%
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

#%%
# make graph
from collections import defaultdict
graph = defaultdict(list)

for start, end in vertex:
    graph[start].append(end)
    graph[end].append(start)

#%%
graph

# %%
shortest = [float('inf')] * (n+1)
start = 1
shortest[0], shortest[start] = 0, 0
#%%
import heapq
q = list()
heapq.heappush(q, (0, 1))
#%%
while q:
    # 탐색 노드, 거리 추출
    dist, current_node = heapq.heappop(q)

    print(f"current_node : {current_node}, dist : {dist}, shortest : {shortest}")
    print(f"q : {q}")

    # 연결된 노드 순회
    for node in graph[current_node]:
        # 기존 최단거리보다 더 짧은 경우, 갱신
        if dist + 1 < shortest[node]:
            shortest[node] = dist + 1 # 거리 갱신
            heapq.heappush(q, (shortest[node], node)) # 순회할 노드에 추가
# %%
shortest
#%%
####################################
########## solution ################
####################################
#%%
from collections import defaultdict
import heapq

def solution(n, edge):
    # make graph
    graph = defaultdict(list)

    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)

    # 최댓값으로 최단거리 리스트 값 초기화
    shortest = [float('inf')] * (n+1)
    start = 1
    shortest[0], shortest[start] = 0, 0

    # 순회할 큐 초기값 세팅
    q = list()
    heapq.heappush(q, (0, 1))

    while q:
        # 탐색 노드, 거리 추출
        dist, current_node = heapq.heappop(q)

        # 연결된 노드 순회
        for node in graph[current_node]:
            # 기존 최단거리보다 더 짧은 경우, 갱신
            if dist + 1 < shortest[node]:
                shortest[node] = dist + 1 # 거리 갱신
                heapq.heappush(q, (shortest[node], node)) # 순회할 노드에 추가
    
    return shortest.count(max(shortest))