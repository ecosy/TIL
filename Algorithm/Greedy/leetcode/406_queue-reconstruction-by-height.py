# https://leetcode.com/problems/queue-reconstruction-by-height/
# leetcode #406
# 그리디
# 키에 따른 대기열 재구성

#%%
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

#%%
people.sort(key=lambda x: (x[1], -x[0]))
people
#%%
answer = []
for p in people:
    push_index = 0
    count = p[1]
    while answer and count > 0:
        if answer[push_index][0] >= p[0]:
            count -= 1
            print(answer[push_index][0], p[0], count)
        push_index += 1

    answer.insert(push_index, p)

    print(p, '  idx : ', push_index)
    print(answer)
    print('__________________________')
answer
#%%

# My Solution
'''
1. (h : 키, k : 자신보다 키 큰, 앞 사람 수)에서 k에 대한 오름차순, h에 대한 내림차순으로 정렬한다.
2. 차례대로 꺼내서 정답배열에 넣는다.
3. 이때, k 명의 자신보다 큰 사람 바로 뒤에 삽입한다. 
* 시간복잡도 : O(n^2)
'''

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 사람의 수에 대한 오름차순, 키에 대한 내림차순 졍렬
        people.sort(key=lambda x: (x[1], -x[0]))

        answer = []
        for p in people:
            push_index = 0 # 삽입할 index
            count = p[1] # 자신보다 큰 사람 수를 셀 변수

            # 자신의 키 이상인 사람의 수가 p[1]개 일때까지 반복하여 push_index 증가
            while answer and count > 0:
                if answer[push_index][0] >= p[0]:
                    count -= 1
                push_index += 1

            answer.insert(push_index, p)
        return answer

#%%

# 책 풀이 분석
# 시간복잡도 : O(n * log n)

from typing import List
import heapq
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        # [키 역순, 삽입 인덱스] 삽입
        for person in people:                             # O(n)
            heapq.heappush(heap, (-person[0], person[1])) # O(logn)
        
        result = []
        # 키 역순, 삽입 인덱스 추출
        while heap:                                       # O(n)
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result