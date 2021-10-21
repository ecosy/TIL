# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    # 가장 작은 요소가 K보다 작은 경우 반복
    while scoville[0] < K:
        # heapq가 2개 이상인 경우
        if len(scoville) >= 2:
            k1 = heapq.heappop(scoville) # 가장 작은 값
            k2 = heapq.heappop(scoville) # 그 다음 작은 값
            
            heapq.heappush(scoville, k1 + k2 * 2)
            answer += 1
            
        # heapq가 1개 이하인 경우
        else:
            answer = -1
            break
    
    if answer == 0 or not scoville:
        return -1
    return answer