# https://programmers.co.kr/learn/courses/30/lessons/60062

# Solving (정합성 92 / 100) 
# Test Case 10, 21 통과 X

'''
<Logic>
1. 가장 많은 dist를 갈 수 있는 친구부터,
그 친구가 갈 수 있는 point의 range를 뽑아내고
해당 range 안에 포함되는 weak 지점의 개수를 세어 count 변수에 더한다.

2. 해당 친구와 weak 지점을 제외한 dist, weak 값을
재귀함수 형태로 다시 넘겨주어
다른 친구들에 대해서도 weak 지점의 개수를 세고 count 변수에 더한다.

3. weak가 더 이상 남아있지 않은 경우 count 변수를 friends_count 리스트에 append시키고, 
최종적으로 friends_count의 min 값을 리턴한다.

만약 dist가 더 이상 남지 않은 경우 -1을 리턴해준다.
'''

##################################################################################################

# 제출 코드

#%%
n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

#%%
def solution(n, weak, dist):
    friends_count = []
    dist.sort()
    def search(weak, dist, friend_count):
        # weak가 더 이상 남지 않은 경우 지금까지의 count 변수를 friends count에 저장함
        if not weak:
            friends_count.append(friend_count)
            return
        # dist, 친구가 남지 않은 경우 아무 것도 저장 안함 -> 뒤에서 예외처리
        if not dist:
            return

        # dist 리스트에서 가장 큰 값 추출
        friend_dist = dist.pop()

        # 해당 친구가 갈 수 있는 외벽 index 저장 변수
        search_range = list()

        # 남아있는 weak 지점에서 출발하여
        # 해당 dist 친구가 갈 수 있는 range 조사
        for start_point in weak:
            search_range.append([ i if i < n else i - n for i in range(start_point, start_point + friend_dist + 1, 1) ])
            search_range.append([ i if i >= 0 else i + n for i in range(start_point - friend_dist, start_point + 1, 1) ])

        # search range 변수에서 
        # 현재 남이있는 weak 지점 중 포함되는 지점과 총 개수를 저장
        included_weak = [] # count, unit
        for r in search_range:
            dic = {
                'count': 0,
                'included_unit' : []
            }
            for w in weak:
                if w in r:
                    dic['count'] += 1
                    dic['included_unit'].append(w)

            # included_weak 변수 내 중복 제거
            if dic not in included_weak:
                included_weak.append(dic)

        # 점검 가능한 weak 지점 개수 중 가장 큰 값 추출
        max_unit_count = max([ dic['count'] for dic in included_weak ])

        # max weak 개수에 해당하는 weak 지점 dictionary 정보 추출
        min_unit_dict = [ dic for dic in included_weak if dic['count'] == max_unit_count]

        # 해당 weak 지점을 제거한 weak 변수와, dist 변수를
        # 재귀 함수로 넘김
        for dic in min_unit_dict:
            new_weak = weak[:]
            for unit in dic['included_unit']:
                new_weak.remove(unit)
            search(new_weak, dist[:], friend_count + 1)

    search(weak, dist, friend_count=0)
    if friends_count:
        return min(friends_count)

    # 모든 경우 weak는 남고, dist는 고갈된 경우, -1 리턴
    else:
        return -1

# %%
solution(n, weak, dist)

##################################################################################################

# 이하는 풀이 과정 기록

#%%
d = 4
[ i if i < n else i - n for i in range(10, 10 + d + 1, 1) ]
#%%
friend_dist = 4
search_range = list()
for start_point in [10]:
    search_range.append([ i if i < n else i - n for i in range(start_point, start_point + friend_dist + 1, 1) ])
    search_range.append([ i if i >= 0 else i + n for i in range(start_point - friend_dist, start_point + 1, 1) ])
search_range

#%%
included_weak = [] # count, unit
for r in search_range:
    dic = {
        'count': 0,
        'included_unit' : []
    }
    for w in weak:
        if w in r:
            dic['count'] += 1
            dic['included_unit'].append(w)
    included_weak.append(dic)
included_weak
#%%
min_count = min([ dic['count'] for dic in included_weak ])
min_count
#%%
[ dic for dic in included_weak if dic['count'] == min_count]

#%%
# n = 12
# weak = [1, 5, 6, 10]
# dist = [1, 2, 3, 4] 
# n = 12
# weak = [1, 3, 4, 9, 10]	
# dist = 	[3, 5, 7]
# n = 200
# weak = [0, 100]
# dist = [1, 1]
# n = 12
# weak = [10, 0]
# dist = [1, 2]
n = 200
weak = [0, 10, 50, 80, 120, 160]
dist = [1, 10, 5, 40, 30]

#%%
friends_count = []
def search(weak, dist, friend_count):
    if not weak:
        friends_count.append(friend_count)
        return
    if not dist:
        return 

    print(f'dist : {dist}, weak: {weak}')
    friend_dist = dist.pop()
    search_range = list()
    print(f'friend dist : {friend_dist}, friend count : {friend_count}')

    for start_point in weak:
        search_range.append([ i if i < n else i - n for i in range(start_point, start_point + friend_dist + 1, 1) ])
        search_range.append([ i if i >= 0 else i + n for i in range(start_point - friend_dist, start_point + 1, 1) ])

    included_weak = [] # count, unit
    for r in search_range:
        dic = {
            'count': 0,
            'included_unit' : []
        }
        for w in weak:
            if w in r:
                dic['count'] += 1
                dic['included_unit'].append(w)
        # 중복 제거
        if dic not in included_weak:
            included_weak.append(dic)

    max_unit_count = max([ dic['count'] for dic in included_weak ])
    min_unit_dict = [ dic for dic in included_weak if dic['count'] == max_unit_count]

    print(search_range)
    print(min_unit_dict)
    print('____________________________________')

    for dic in min_unit_dict:
        new_weak = weak[:]
        for unit in dic['included_unit']:
            new_weak.remove(unit)
        search(new_weak, dist[:], friend_count + 1)
#%%
search(weak, dist, friend_count=0)
friends_count

