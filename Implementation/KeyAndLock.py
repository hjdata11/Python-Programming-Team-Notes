# 자물쇠와 열쇠
# https://programmers.co.kr/learn/courses/30/lessons/60059

from copy import deepcopy

def rotation(key):
    tmp_key = []
    for v in zip(*key[::-1]):
        tmp_key.append(v)
    
    return tmp_key

def solution(key, lock):
    
    k = len(key)
    l = len(lock)
    
    new_lock = [[0] * (2*k + l) for _ in range(2*k + l)]
    
    for i in range(l):
        for j in range(l):
            new_lock[k+i][k+j] = lock[i][j]
    
    tmp_lock = deepcopy(new_lock)
    
    for i in range(k+l+1):
        for j in range(k+l+1):
            
            for _ in range(4):
                for x in range(k):
                    for y in range(k):
                        tmp_lock[i+x][j+y] += key[x][y]
                
                S = 0
                for x in range(l):
                    for y in range(l):
                        if tmp_lock[k+x][k+y] == 1:
                            S += 1
                
                if S == l*l:
                    return True
                
                key = rotation(key)
                tmp_lock = deepcopy(new_lock)

    return False