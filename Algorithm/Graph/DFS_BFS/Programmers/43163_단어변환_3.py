# https://programmers.co.kr/learn/courses/30/lessons/43163
# 프로그래머스
# 단어변환
# 3번째 풀이

#%%
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
# %%
# visited = []
counts = []
# %%
def dfs(word, visited):
    # target에 도달한 경우 종료
    if word == target:
        counts.append(len(visited))
        return
    
    for _word in words:
        if _word == word:
            continue
        
        # 서로 다른 자릿수 카운트
        diff_count = 0
        for i in range(len(_word)):
            if _word[i] != word[i]:
                diff_count += 1

        # 한 자리만 다르고, 방문하지 않은 단어인 경우
        if diff_count == 1 and _word not in visited:
            visited.append(_word)
            dfs(_word, visited)
            visited.pop()

#%%
dfs(begin, [])
# %%
counts

#%%
min(counts)

#%%
def solution(begin, target, words):
    
    def dfs(word, visited):
        # target에 도달한 경우 종료
        if word == target:
            counts.append(len(visited))
            return
        
        for _word in words:
            if _word == word:
                continue
            
            # 서로 다른 자릿수 카운트
            diff_count = 0
            for i in range(len(_word)):
                if _word[i] != word[i]:
                    diff_count += 1

            # 한 자리만 다르고, 방문하지 않은 단어인 경우
            if diff_count == 1 and _word not in visited:
                visited.append(_word)
                dfs(_word, visited)
                visited.pop()

    # target이 words에 존재하지 않는 경우 조기 종료
    if target not in words:
        return 0

    counts = []
    dfs(begin, [])

    # target이 words에 존재하지만 변환 불가능한 경우
    if not counts:
        return 0

    return min(counts)