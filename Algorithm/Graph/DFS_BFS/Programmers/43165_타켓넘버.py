# https://programmers.co.kr/learn/courses/30/lessons/43165
# 프로그래머스
# BFS/DFS
# 타겟넘버

#%%
# My Solution
# DFS로 각각의 리스트 요소에 대해 +, - 경우를 계산하고
# target과 일치하는 횟수를 센다.

answer = 0
def solution(numbers, target):
    def dfs(path, index):
        global answer
        
        # DFS로 리스트 끝요소까지 탐색한 경우
        if len(path) == len(numbers):
            # target과 비교
            if sum(path) == target:
                answer += 1
            return

        # '+' 방향으로 탐색
        path.append(numbers[index])
        index += 1
        dfs(path, index)
        index -= 1
        path.pop()

        # '-' 방향으로 탐색
        path.append(numbers[index] * (-1))
        index += 1
        dfs(path, index)
        index -= 1
        path.pop()

    dfs(path = [], index = 0)
    return answer