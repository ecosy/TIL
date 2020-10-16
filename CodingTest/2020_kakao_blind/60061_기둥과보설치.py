bo = []
gi = []
GI = 0
BO = 1

def insertion_check(_type, x, y):
    # 기둥인 경우
    if _type == GI:
        # (1) 바닥 위인 경우
        if y == 0:
            return True
        
        # (2) 보 위에 있는 경우
        for _bo in bo: # _bo : [[x, y], [x, y + 1]]
            if [x, y] in _bo:
                return True

        # (3) 다른 기둥 위인 경우
        for _, _gi in gi:
            if [x, y] == _:
                continue
            if [x, y] == _gi:
                return True

        # (4) 모두 아닌 경우 
        return False
    
    # 보 인 경우
    else:
        _count = 0
        # (1) 양쪽이 다른 보와 연결된 경우
        for _bo1, _bo2 in bo:
            # 자기 자신인 경우 제외
            if [[x, y], [x + 1, y]] == [_bo1, _bo2]:
                continue
            elif [x, y] == _bo2 or [x + 1, y] == _bo1:
                _count += 1
        if _count == 2:
            return True
        
        # (2) 기둥 위인 경우
        for _, _gi in gi:
            if [x, y] == _gi or [x + 1, y] == _gi:
                return True
            
        # (3) 모두 아닌 경우
        return False

def deletion_check():
    # 기둥 체크
    for _gi, _ in gi:
        if not insertion_check(GI, _gi[0], _gi[1]):
            return False
    # 보 체크
    for _bo, _ in bo:
        if not insertion_check(BO, _bo[0], _bo[1]):
            return False
    return True
    
    
def solution(n, build_frame):
    # answer = [[]]
    # return answer
    
    for x, y, a, b in build_frame:
        # 설치 시
        if b == 1:
            if insertion_check(a, x, y):
                if a == GI: # 기둥
                    gi.append([[x, y], [x, y + 1]])
                    
                else: # 보
                    bo.append([[x, y], [x + 1, y]])
        # 삭제 시
        else:
            if a == GI: # 기둥
                gi.remove([[x, y], [x, y + 1]])
                if not deletion_check():
                    gi.append([[x, y], [x, y + 1]])
                
            else : # 보
                bo.remove([[x, y], [x + 1, y]])        
                if not deletion_check():
                    bo.append([[x, y], [x + 1, y]]) 
            
    answer = []
    for _bo, _ in bo:
        _bo.append(BO)
        answer.append(_bo)
    for _gi, _ in gi:
        _gi.append(GI)
        answer.append(_gi)

    if not answer:
        return [[]]
    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))