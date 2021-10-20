'''
가장 바깥의 x, y 좌표를 찾으면 됨

왼쪽 x1 오른쪽 x2
아래쪽 y1 위쪽 y2

left_x, right_x
low_y, high_y

bottom = right_x - left_x
height = high_y - low_y

area = bottom * height

...
색깔별로 그룹을 나누고, 
각 그룹에서 하나씩 브루트포스 서치 조합을 구하기

그 중에서 최소 면적 구하기

'''

#%%

N = 5
K = 2
spots = [
    [-4, -2, 1],
    [-5, -3, 1],

    [5, -4 , 2],
    [4, -5 , 2],
    [3, -8, 2],

]

#%%
N = 5
K = 3
spots = [
    [3, 7, 1],
    [5, 8, 1],

    [6, 5 , 2],
    [7, 1 , 3],
    [9, 3, 3],
]

#%%
N = 7
K = 3
spots = [
    [-4, 0, 1],
    [-5, -1, 1],
    [0, 43, 2],
    [3, 23, 3],
    [8, -19, 2],
    [10, 0, 3],
    [20, 0, 2]
]

# %%
# 각 점들의 그룹에서 하나씩 모든 경우의 수를 뽑아오는 것
# dfs로 서치
#%%
from collections import defaultdict
color_spots = defaultdict(list)
#%%
for spot in spots:
    color_spots[spot[-1]].append(spot[:-1])
#%%

#%%
def CalculateArea(X : list, Y : list) -> int:
    X.sort()
    Y.sort()
    min_x, max_x = X[0], X[-1]
    min_y, max_y = Y[0], Y[-1]
    print(f"min x : {min_x}, max_x : {max_x}, min y : {min_y}, max y : {max_y}")
    print(f"area : {(max_x - min_x) * (max_y - min_y)}")
    return (max_x - min_x) * (max_y - min_y)
#%%
min_area = float('inf')
min_area
#%%
_count = 0
def dfs(comb, keys):
    print(f"keys : {keys}, comb : {comb}")

    if not keys :
        print(f"------------------------ comb : {comb}")
        global min_area
        area = CalculateArea(comb['x'][:], comb['y'][:])
        min_area = min(min_area, area)
        print(f"area : {area}, min_area : {min_area}")
        print("------------------------")
        global _count
        _count += 1
        return

    else:
        next_key_index = keys.pop()
        for _value_index in range (len(color_spots[next_key_index])):
            # comb['x'].append()
            x = color_spots[next_key_index][_value_index][0]
            y = color_spots[next_key_index][_value_index][1]

            comb['x'].append(x)
            comb['y'].append(y)

            dfs(comb, keys[:])
            
            comb['x'].pop()
            comb['y'].pop()
#%%
keys = list(color_spots.keys())
keys.sort()
keys
# %%
first_key = keys.pop(0)
for x, y in color_spots[first_key]:
    comb = dict()
    comb['x'] = [x]
    comb['y'] = [y]
    dfs(comb, keys[:])
# %%
min_area
# %%
_count
#%%
############################
# solution 1
###########################

import sys
from collections import defaultdict

N, K = map(int, input().split())
spots = list()
for _ in range(N):
    spots.append(list(map(int, input().split())))

min_area = float('inf')

# 두 점 사이 직사각형 넓이를 구한다.
def CalculateArea(X : list, Y : list) -> int:
    X.sort()
    Y.sort()
    min_x, max_x = X[0], X[-1]
    min_y, max_y = Y[0], Y[-1]
    return (max_x - min_x) * (max_y - min_y)

# 색깔별 점들의 조합을 구하고, 그들의 넓이를 구한다.
def dfs(comb, keys):
    if not keys :
        global min_area
        area = CalculateArea(comb['x'][:], comb['y'][:])
        min_area = min(min_area, area)
        return

    else:
        next_key_index = keys.pop()
        for _value_index in range (len(color_spots[next_key_index])):
            x = color_spots[next_key_index][_value_index][0]
            y = color_spots[next_key_index][_value_index][1]

            comb['x'].append(x)
            comb['y'].append(y)

            dfs(comb, keys[:])
            
            comb['x'].pop()
            comb['y'].pop()

# 색깔별 좌표 dictionary 구성
# key : 색깔 번호, value : 좌표 리스트
color_spots = defaultdict(list)
for spot in spots:
    color_spots[spot[-1]].append(spot[:-1])

keys = list(color_spots.keys())
keys.sort()

first_key = keys.pop(0)
for x, y in color_spots[first_key]:
    comb = dict()
    comb['x'] = [x]
    comb['y'] = [y]
    dfs(comb, keys[:])

print(min_area)

#%%
############################
# solution 2
# function call 줄임
###########################

import sys
from collections import defaultdict

N, K = map(int, input().split())
spots = list()
for _ in range(N):
    spots.append(list(map(int, input().split())))

min_area = float('inf')

# 색깔별 점들의 조합을 구하고, 그들의 넓이를 구한다.
def dfs(comb, keys):
    if not keys :
        global min_area
        _X = sorted(comb['x'])
        _Y = sorted(comb['y'])
        min_area = min(min_area, (_X[-1] - _X[0]) * (_Y[-1] - _Y[0]))
        return

    else:
        next_key_index = keys.pop()
        for _value_index in range (len(color_spots[next_key_index])):
            x = color_spots[next_key_index][_value_index][0]
            y = color_spots[next_key_index][_value_index][1]

            comb['x'].append(x)
            comb['y'].append(y)

            dfs(comb, keys[:])
            
            comb['x'].pop()
            comb['y'].pop()

# 색깔별 좌표 dictionary 구성
# key : 색깔 번호, value : 좌표 리스트
color_spots = defaultdict(list)
for spot in spots:
    color_spots[spot[-1]].append(spot[:-1])

keys = list(color_spots.keys())
keys.sort()

first_key = keys.pop(0)
for x, y in color_spots[first_key]:
    comb = dict()
    comb['x'] = [x]
    comb['y'] = [y]
    dfs(comb, keys[:])

print(min_area)
