
# https://www.acmicpc.net/problem/17822

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, m, t = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]
visited = [[0]*m for _ in range(n)]
total = sum([sum(v) for v in data])
numbers = n * m

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 회전
def rotate():
    global data

    x, d, k = map(int, input().split())
    for i in range(1, n+1):
        if i % x == 0:
            i -= 1
            if d == 0:
                data[i] = data[i][-k:] + data[i][:-k]
                visited[i] = visited[i][-k:] + visited[i][:-k]
            else:
                data[i] = data[i][k:] + data[i][:k]
                visited[i] = visited[i][k:] + visited[i][:k]

# 원판에서 인접한 같은 수의 개수를 구함
def bfs(x, y):

    q = deque()
    q.append([x, y])
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if ny == m:
                ny = 0
            if ny < 0:
                ny = m-1

            if 0 <= nx < n and 0 <= ny < m :
                if visited[nx][ny] == 0 and data[x][y] == data[nx][ny]:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                    count += 1

    return count

for i in range(t):
    rotate()
    flag = True
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                cnt = bfs(i, j)
                if cnt:
                    total -= data[i][j] * cnt
                    numbers -= cnt
                    flag = False

    if numbers == 0:
        total = 0
        break
    if flag:
        avg = total / numbers
        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    if data[i][j] > avg:
                        data[i][j] -= 1
                        total -= 1
                    elif data[i][j] < avg:
                        data[i][j] += 1
                        total += 1

print(total)