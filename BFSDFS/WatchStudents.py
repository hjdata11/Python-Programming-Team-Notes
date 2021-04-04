
# https://www.acmicpc.net/problem/18428

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


n = int(input())
data = [ list(map(str, input().split())) for _ in range(n) ]
teachers = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if data[i][j] == 'T':
            teachers.append((i, j))

# 학생 감시
def watch(x, y, dir):
    if dir == 0:
        while y >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1
    if dir == 1:
        while y < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1
    if dir == 2:
        while x >= 0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1
    if dir == 3:
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1

    return False

# 선생님들 학생 감시
def process():
    for x, y in teachers:
        for i in range(4) :
            if watch(x, y, i):
                return True
    return False

find = False
# 빈 공간에서 3개를 뽑는 모든 조합 확인
def dfs(cnt):
    global find
    if cnt == 3:
        if not process():
            find = True
        return

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                data[i][j] = 'O'
                dfs(cnt + 1)
                data[i][j] = 'X'

dfs(0)

if find:
    print('YES')
else:
    print('NO')
