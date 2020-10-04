# https://leetcode.com/problems/network-delay-time/
# leetcode #743
# shortest path
# network delay time

#%%

# 풀이 과정

# times = [[2,1,1],[2,3,1],[3,4,1]]
# N = 4
# K = 2

# times = [[1,2,1]]
# N = 2
# K = 2

times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
N = 2
K = 1

# %%
# list to dict
import collections
graph = collections.defaultdict(list)
nodes = set()
for _start, _end, _weight in times:
    graph[_start].append([_end, _weight])
    nodes.add(_start)
    nodes.add(_end)
graph
#%%
nodes
# %%
import heapq
def dijkstra(graph, start_v):
    # 초기화
    shortest_path = {node: float('inf') for node in nodes}
    shortest_path[start_v] = 0
    print(shortest_path)
    # priority queue 초기화
    queue = []
    heapq.heappush(queue, [shortest_path[start_v], start_v])
    
    # heapq 탐색
    while queue:
        current_weight, current_node = heapq.heappop(queue)

        # 이미 저장된 최소 값보다 클 경우 continue
        if current_weight > shortest_path[current_node]:
            continue
        
        # current_node와 연결된 노드에 대해 최소 값 업데이트
        for _node, _weight in graph[current_node]:
            new_distance = current_weight + _weight
            print('new dist : ', new_distance)
            print('shortest_path[_node] : ', shortest_path[_node])

            if new_distance < shortest_path[_node]:
                shortest_path[_node] = new_distance

                print(new_distance, _node)
                heapq.heappush(queue, [new_distance, _node])
    return shortest_path
# %%
shortest = dijkstra(graph, K)
#%%
shortest
#%%
values = shortest.values()
if float('inf') in values:
    print(-1)
else:
    print(max(values))

#%%

# My Solution

import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        nodes = set()
        for _start, _end, _weight in times:
            graph[_start].append([_end, _weight])
            nodes.add(_start)
            nodes.add(_end)

        def dijkstra(graph, start_v):
            # 초기화
            shortest_path = {node: float('inf') for node in nodes}
            shortest_path[start_v] = 0

            # priority queue 초기화
            queue = []
            heapq.heappush(queue, [shortest_path[start_v], start_v])

            # heapq 탐색
            while queue:
                current_weight, current_node = heapq.heappop(queue)

                # 이미 저장된 최소 값보다 클 경우 continue
                if current_weight > shortest_path[current_node]:
                    continue
                
                # current_node와 연결된 노드에 대해 최소 값 업데이트
                for _node, _weight in graph[current_node]:
                    new_distance = current_weight + _weight

                    if new_distance < shortest_path[_node]:
                        shortest_path[_node] = new_distance

                        heapq.heappush(queue, [new_distance, _node])
            return shortest_path

        shortest = dijkstra(graph, K)

        values = shortest.values()
        if float('inf') in values:
            return -1
        return max(values)

#%%

# 책 풀이 분석

import collections
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # 그래프 인접 리스트 구성
        for u, v, w in times:
            graph[u].append((v, w))
        
        # 큐 변수 : [(소요 시간, 정점)]
        Q = [(0, K)]

        dist = collections.defaultdict(int)

        # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
        while Q:
            time, node = heapq.heappop(Q)
            # 가장 먼저 입력된 경로가 무조건 최단경로 이므로
            # 그 이후의 node 값은 버림
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        # 모든 노드의 최단 경로 존재 여부 판별
        if len(dist) == N:
            return max(dist.values())
        return -1