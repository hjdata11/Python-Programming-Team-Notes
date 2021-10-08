
# www.acmicpc.net/problem/16234

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]
count = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 인구 이동
def move(x, y, union_index):

    united = []
    united.append((x, y))

    union[x][y] = union_index
    q = deque()
    q.append((x, y))
    S = data[x][y]
    union_count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and union[nx][ny] == -1:
                if l <= abs(data[nx][ny] - data[x][y]) <= r:
                    S += data[nx][ny]
                    union_count += 1
                    united.append((nx, ny))
                    union[nx][ny] = union_index
                    q.append((nx, ny))

    for x, y in united:
        avg = int(S/union_count)
        data[x][y] = avg

# 인구 이동 종료 체크
while True:
    # 연합 종류
    union = [ [-1] * n for _ in range(n) ]
    union_index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                move(i, j, union_index)
                union_index += 1

    if union_index == n*n:
        break
    count += 1

print(count)