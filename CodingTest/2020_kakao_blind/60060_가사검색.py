# https://programmers.co.kr/learn/courses/30/lessons/60060

# Solving (70 / 100)
# 정확성 Test Case 통과 O
# 효율성 Test Case 4, 5 통과 X

'''
<Logic>
- Concept : 각 단어가 가질 수 있는 Query를 key로 갖는 hash 자료구조를 사용한다.

1. 각 단어가 가질 수 있는 Query 조합을 구한다. 
(e.g.) fro -> f?, fr?, ???, ?ro, ??o

2. 각 조합을 Key로 갖는 Dictionary를 만들고, 해당 key가 생성될 때마다 value 값을 + 1 더해준다.

3. Query를 돌며, 해당 query를 key로 갖는 value 값을 answer로 리턴한다.

'''

##################################################################################################

# 제출 코드

#%%
def solution(words, queries):
    hash_dict = {}

    # 각 단어가 가질 수 있는 query 조합을 모두 hash_dict에 넣고,
    # 해당 query를 가질 때마다 +1씩 더함
    for word in words:
        w_length = len(word)
        for i in range(w_length):
            
            # (e.g.) f??, fr?, ???
            hash_key = word[:i] + '?'*(w_length - i)

            if hash_key in hash_dict:
                hash_dict[hash_key] += 1
            else:
                hash_dict[hash_key] = 1

            # 마지막 key값들의 중복 피하기 (모두 ? 문자인 경우)
            if i == w_length - 1:
                break
            
            # (e.g.) ?ro, ??o
            reverse_hash_key = '?'*(i+1) + word[i+1:]
            if reverse_hash_key in hash_dict:
                hash_dict[reverse_hash_key] += 1
            else:
                hash_dict[reverse_hash_key] = 1
    
    # query에 해당하는 value 값을 answer에 넣기
    answer = []
    for q in queries:
        if q not in hash_dict:
            answer.append(0)
        else:
            answer.append(hash_dict[q])
    return answer

#%%
##################################################################################################

# 이하는 풀이 과정 기록

#%%
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

# %%
hash_dict = {}

for word in words:
    w_length = len(word)
    for i in range(w_length):
        hash_key = word[:i] + '?'*(w_length - i)

        if hash_key in hash_dict:
            hash_dict[hash_key] += 1
        else:
            hash_dict[hash_key] = 1

        # 마지막 key값들의 중복 피하기
        if i == w_length - 1:
            break
        
        reverse_hash_key = '?'*(i+1) + word[i+1:]
        if reverse_hash_key in hash_dict:
            hash_dict[reverse_hash_key] += 1
        else:
            hash_dict[reverse_hash_key] = 1
hash_dict

#%%
answer = []
for q in queries:
    if q not in hash_dict:
        answer.append(0)
    else:
        answer.append(hash_dict[q])
answer

#%%
w = 'frodo'
w_length = len(w)
for i in range(w_length):
    hash_key = w[:i] + '?'*(w_length - i)

    if hash_key in hash_dict:
        hash_dict[hash_key] += 1
    else:
        hash_dict[hash_key] = 0

    # 마지막 key값들의 중복 피하기
    if i == w_length - 1:
        break
    
    reverse_hash_key = '?'*(i+1) + w[i+1:]
    if reverse_hash_key in hash_dict:
        hash_dict[reverse_hash_key] += 1
    else:
        hash_dict[reverse_hash_key] = 0
hash_dict

#%%
length = len(w)
w[:1] + '?'*(length - 1)