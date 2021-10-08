
# https://www.acmicpc.net/problem/14502

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

viruses = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            viruses.append([i, j])

# 빈 개수 세기
def count_num():
    global result
    S = 0
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 0:
                S += 1

    result = max(S, result)

# 바이러스 퍼트리기
def virus_spread(x, y):

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if tmp_data[nx][ny] == 0:
                    tmp_data[nx][ny] = 2
                    q.append([nx, ny])

# 기둥 세우기
def dfs(count):
    global result
    global tmp_data
    if count == 3:
        tmp_data = deepcopy(data)
        # 바이러 전파 진행
        for i, j in viruses:
            virus_spread(i, j)
        count_num()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from copy import deepcopy

n, m = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

viruses = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            viruses.append([i, j])

# 빈 개수 세기
def count_num():
    global result
    S = 0
    for i in range(n):
        for j in range(m):
            if tmp_data[i][j] == 0:
                S += 1

    result = max(S, result)

# 바이러스 퍼트리기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            # 벽이 아닌 경우
            if tmp_data[nx][ny] == 0:
                tmp_data[nx][ny] = 2
                virus(nx, ny)

# 기둥 세우기
def dfs(count):
    global result
    global tmp_data
    if count == 3:
        tmp_data = deepcopy(data)
        # 바이러 전파 진행
        for i, j in viruses:
            virus(i, j)
        count_num()
        return

    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)