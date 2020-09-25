# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# 리트코드
# 그리디 
# 주식을 사고팔기 가장 좋은 시점 2

'''
[구매]
1. 가장 쌀 때 주식을 사야 함

[판매]
1. 가장 비쌀 때 주식을 팔아야 함
2. 주식을 산 가격보다 비싸야 함

'''
#%%
# 풀이 과정

# prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
# prices = [7,6,4,3,1]
prices = [6,1,3,2,4,7]

#%%
available_stocks = []
#%%
for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if prices[i] < prices[j]:
            available_stocks.append([i, j]) # 구입, 판매 요소 index 저장
available_stocks.sort(key=lambda x: (x[0], -x[1]))
available_stocks
#%%
profits = []
#%%
for i in range(len(available_stocks)):

    buy_index = available_stocks[i][0]
    sell_index = available_stocks[i][1]
    print('start point : ', buy_index, sell_index)

    profit = prices[sell_index] - prices[buy_index] # 첫 주식의 이익 계산

    for j in range(len(available_stocks)):
        if i == j:
            continue
        # 이전 주식 판매 시점 이후에 주식 구입 시점이 있다면
        if available_stocks[j][0] > sell_index:
            profit += prices[available_stocks[j][1]] - prices[available_stocks[j][0]]
            
            # 주식 판매시점 업데이트
            sell_index = available_stocks[j][1]

            print(available_stocks[j][0], available_stocks[j][1])
    print('______________________________________________')
    profits.append(profit)
profits



#%%

# My Solution -> 일부 테스트 케이스 통과 못함

# 구입, 판매 할 수 있는 구간의 인덱스를 구하고
# 가능한 인덱스 조합을 구하고, 그 중에서 주식 합이 MAX인 값을 리턴한다.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        available_stocks = []
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[i] < prices[j]:
                    available_stocks.append([i, j]) # 구입, 판매 요소 index 저장

        available_stocks.sort(key=lambda x: (x[0], -x[1]))

        profits = []
        for i in range(len(available_stocks)):
        
            buy_index = available_stocks[i][0]
            sell_index = available_stocks[i][1]

            profit = prices[sell_index] - prices[buy_index] # 첫 주식의 이익 계산

            for j in range(len(available_stocks)):
                if i == j:
                    continue
                # 이전 주식 판매 시점 이후에 주식 구입 시점이 있다면
                if available_stocks[j][0] > sell_index:
                    profit += prices[available_stocks[j][1]] - prices[available_stocks[j][0]]

                    # 주식 판매시점 업데이트
                    sell_index = available_stocks[j][1]

            profits.append(profit)
        if profits:
            return max(profits)
        return 0

#%%

# 책 풀이 분석 1

# 각 구간에서 이전보다 주식이 증가했으면 무조건 합에 더했다.
# 이전보다 떨어지지만 않는다면 되기 때문이다.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        # 값이 오르는 경우 매번 그리디 계산
        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[i]:
                result += prices[i + 1] - prices [i]
        return result

#%%
s = Solution()
s.maxProfit(prices)
#%%

# 책 풀이 분석 2
# 파이썬다운 방식

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0보다 크면 무조건 합산
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))