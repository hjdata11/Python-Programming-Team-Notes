
# https://programmers.co.kr/learn/courses/30/lessons/60058

def balanced(w):
    cnt = 0
    for i, v in enumerate(w):
        if v == "(":
            cnt += 1
        if v == ")":
            cnt -= 1
        if cnt == 0:
            return i

def is_right(w):
    tmp = []
    for v in w:
        if v == "(":
            tmp.append(v)
        else:
            if tmp:
                tmp.pop()
            else:
                return False
    if tmp:
        return False
    return True

def solution(w):
    
    # 1. 빈 문자열인 경우, 올바른 문자열일 경우 반환
    if w == "" or is_right(w) : return w
    
    # 2. 균형잡힌 괄호 문자열로 분리
    u, v = w[:balanced(w)+1], w[balanced(w)+1:]
    
    # 3. u 올바른 문자열
    if is_right(u):
        S = solution(v)
        return u + S
    #4. u 올바른 문자열 X
    else:
        T = "("
        T += solution(v)
        T += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            elif u[i] == ")":
                u[i] = "("
        T += "".join(u)
        return T