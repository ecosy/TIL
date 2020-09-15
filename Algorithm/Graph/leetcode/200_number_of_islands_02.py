# https://leetcode.com/problems/number-of-islands/
# 리트코드
# 섬의 개수

# 2번째 풀이

'''
1. 위, 아래, 오른쪽, 왼쪽 방향으로 DFS 탐색을 하면서
탐색한 부분의 값을 1 -> 0 으로 바꾼다.

2. 한 영역에 대한 탐색이 끝나면, 아직 탐색하지 않은 좌표를 탐색한다.
-> 이 문제는 탐색한 좌표를 저장할 필요없다. 1인 부분만 탐색하면 되기 때문이다.

시간 복잡도 : O(NM)
N : grid의 세로 길이
M : grid의 가로 길이
'''

# My Solution
#%%
# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
grid = [
  ["1","1","0","1","0"],
  ["1","1","0","1","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","1"]
]
# %%

def dfs(i, j):
    visitied = []
    stack = [[i, j]] # dfs 시작 좌표 삽임

    while stack:
        x, y = stack.pop() # x, y 좌표 방문

        if [x, y] not in visitied:
            visitied.append([x, y])
            grid[x][y] = "0" # 방문한 곳은 0 으로 초기화

            # 아래 방향 검사
            if x + 1 < len(grid) and grid[x + 1][y] == "1":
                stack.append([x + 1, y])
            
            # 오른쪽 방향 검사
            if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
                stack.append([x, y + 1])
    return

#%%
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(i, j)
        if grid[i][j] == "1":
            print('dfs')
            count += 1
            dfs(i, j)
# %%
count