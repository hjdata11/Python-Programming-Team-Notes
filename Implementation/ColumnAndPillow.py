# https://programmers.co.kr/learn/courses/30/lessons/60061

# 설치가 가능한지 체크
def check(ans):
    for x, y, what in ans:
        # 기둥
        if what == 0:
            if y == 0 or [x-1, y, 1] in ans or [x, y, 1] in ans or [x, y-1, 0] in ans:
                continue
            else:
                return False
        # 보
        if what == 1:
            if [x, y-1, 0] in ans or [x+1, y-1, 0] in ans or ([x-1, y, 1] in ans and [x+1, y, 1] in ans):
                continue
            else:
                return False
    return True
                
def solution(n, build_frame):
    answer = []
    
    # 설치 & 삭제
    for frame in build_frame:
        if frame[3] == 1:
            answer.append(frame[:3])
            if not check(answer):
                answer.remove(frame[:3])
        else:
            answer.remove(frame[:3])
            if not check(answer):
                answer.append(frame[:3])
    
    answer.sort()
    return answer