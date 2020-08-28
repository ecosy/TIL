# https://leetcode.com/problems/number-of-islands/
# 리트코드
# 섬의 개수

'''
1. 위, 아래, 오른쪽, 왼쪽 방향으로 DFS 탐색을 하면서
탐색한 부분의 값을 1 -> 0 으로 바꾼다.

2. 한 영역에 대한 탐색이 끝나면, 아직 탐색하지 않은 좌표를 탐색한다.
-> 이 문제는 탐색한 좌표를 저장할 필요없다. 1인 부분만 탐색하면 되기 때문이다.
'''

# My Solution
#%%
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# %%
from typing import *
unvisited_points: List[List[int, int]] = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            unvisited_points.append((i, j))
unvisited_points
# %%
direction = {
    'up' : [0, -1],
    'down' : [0, 1],
    'left' : [-1, 0],
    'right' : [1, 0]
}

def search(point: List[int, int], count: int, visited: List[List[int, int]]):
    if point == (0,0):
        count = 0

    if grid[point[0], point[1]] == 0:
        return
    else:
        pass
        # up
        # down
        # left
        # right
        # -> 이 부분에서 4방향으로 이동하는 것과 DFS 연결짓지 못했다.
#%%
# 풀이 분석
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # grid 범위 밖으로 나가거나,
            # 해당 값이 1이 아닌 경우 탐색 종료
            if  i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                return

            # 현재 방문한 위치의 값을 0으로 바꾼다.
            grid[i][j] = 0 

            # 4방향에 대한 DFS 탐색
            dfs(i+1, j) # left
            dfs(i, j+1) # down
            dfs(i-1, j) # right
            dfs(i, j-1) # up
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 좌표 값이 1인 경우에만 DFS 탐색을 실시함
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count