# https://programmers.co.kr/learn/courses/30/lessons/60061

def check(answer):
    for x, y, what in answer:
        # 기둥
        if what == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            else:
                return False
        # 보
        elif what == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True
                
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        if frame[3] == 1:
            answer.append(frame[:3])
            if not check(answer):
                answer.remove(frame[:3])
        elif frame[3] == 0:
            answer.remove(frame[:3])
            if not check(answer):
                answer.append(frame[:3])
    answer.sort()
    return answer