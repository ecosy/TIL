# https://leetcode.com/problems/gas-station/
# leetcode #134
# 주유소
# 그리디

#%%
# 풀이 과정
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
# %%
surplus = []
for i, j in zip(gas, cost):
    surplus.append(i - j)
surplus
# %%
if sum(surplus) < 0:
    print(-1)
else:
    last_minus_index = -1
    for i in range(len(surplus)):
        if surplus[i] < 0:
            last_minus_index = i
    if last_minus_index != -1:
        print(last_minus_index + 1)
# %%

# My Solution
# 해결 못함

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = []
        for i, j in zip(gas, cost):
            surplus.append(i - j)

        surplus_sum = sum(surplus)
        if surplus_sum >= 0:
            for i in range(len(surplus)):
                if surplus[i] > 0:
                    j = i
                    _sum = surplus[i]
                    while True:
                        if j == len(surplus):
                            j = 0
                        if surplus[i] + surplus[i + 1] < 0:
                            break
                        
                        j += 1

                    return i
        return -1
#%%
# 책 풀이 분석 1 - 전체 탐색
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    
    # 모든 지점에 대해 탐색
    for start in range(len(gas)):

        fuel = 0
        # start index 부터 한 바퀴 탐색
        for i in range(start, len(gas) + start):
            index = i % len(gas)

            can_travel = True
            if gas[index] + fuel < cost[index]:
                can_travel = False
                break
            else:
                fuel += gas[index] - cost[index]
        if can_travel:
            return start
    return -1
#%%
# 책 풀이 분석 2 - 
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # 모든 주유소 방문 가능 여부 판별
    if sum(gas) < sum(cost):
        return -1
    
    start, fuel = 0, 0
    for i in range(len(gas)):
        # 출발점이 안 되는 지점 판별
        if gas[i] + fuel < cost[i]:
            start = i + 1
            fuel = 0
        else:
            fuel += gas[i] - cost[i]
    return start