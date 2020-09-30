# https://leetcode.com/problems/task-scheduler/
# leetcode
# 그리디
# 테스크 스케줄러

# 해결 못하고 책 풀이 분석함

#%%
tasks = ["A","A","A","B","B","B"]
n = 2
# tasks = ["A","A","A","B","B","B"]
# n = 0
# tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
# n = 2

#%%
from collections import Counter
count = Counter(tasks)
count
# %%
import heapq
heap = []
# %%
for _item, _count in count.items():
    heapq.heappush(heap, ((-1) * _count, _item))
heap
#%%
answer = 0
window = []
_answer = []

if n == 0:
    answer = len(tasks)
answer
#%%
while heap:
    print(f'heap : ', heap)
    answer += 1

    item = None
    # 초반 window 크기가 n보다 작을 때
    if len(window) < n:
        # window 공백 수가 heap의 문자 수보다 많다면
        if window.count("") >= len(heap):
            # 공백 추가
            window.append("")
            _answer.append("") # 삭제
            print('case 1-1')
            print(f'_answer : {_answer}')

        else:
            _temp = []
            while True:
                item = heapq.heappop(heap)
                # window에 문자가 이미 존재하는 경우에만 _temp 저장
                if item[1] in window:
                    _temp.append((item[0], item[1]))
                
                # window에 없는 문자를 찾아 삽입하기
                if item[1] not in window:
                    window.append(item[1])

                    _answer.append(item[1])
                    print(f'_answer : {_answer}')

                    # _temp -> heap 복원
                    for _item in _temp:
                        heapq.heappush(heap, _item)
                    break
            print('case 1-2')
            
        print(f'case 1, window : {window}')

    # window 수 == n 인 경우
    else:
        item = heapq.heappop(heap)
        if item[1] in window:
            window.remove(item[1])
            window.append("")
            print(f'case 2, window : {window}')
            _answer.append("")
            print(f'_answer : {_answer}')
        else:
            window.pop(0)
            window.append(item[1])
            print(f'case 3, window : {window}')
            _answer.append(item[1])
            print(f'_answer : {_answer}')

    if item and item[0] < -1:
        heapq.heappush(heap, (item[0] + 1, item[1]))

    print(f'answer : {answer}')
    print(f'heap {heap}')
    print('___________________')
answer
# %%

# 책 풀이 분석
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            sub_count = 0
            
            # 개수 많은 순서로 추출
            # (n + 1)개 만큼 추출하여 불필요한 idle 수를 제거
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter.subtract(task)
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break
            
            # 필요한 idle 개수를 더함
            result += n - sub_count + 1
        
        return result