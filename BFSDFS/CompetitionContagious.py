
# https://www.acmicpc.net/problem/18405

import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
map = [ list(map(int, input().split())) for _ in range(n) ]
a = input().split()
target, x, y = int(a[0]), int(a[1]), int(a[2])
location = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():
    global map
    q = deque(location)

    while q:
        virus, s, x, y = q.popleft()
        if s == target:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n and map[nx][ny] == 0:
                map[nx][ny] = virus
                q.append([virus, s+1, nx, ny])

for i in range(n):
    for j in range(n):
        if map[i][j] > 0:
            location.append([map[i][j], 0, i, j])

location.sort()

bfs()
print(map[x-1][y-1])