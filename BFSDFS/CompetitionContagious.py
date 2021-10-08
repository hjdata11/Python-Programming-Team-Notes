
# https://www.acmicpc.net/problem/18405

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]
tmp = input().split()
s, x, y = int(tmp[0]), int(tmp[1]), int(tmp[2])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

viruses = []

# 낮은 바이러스부터 증식
def bfs():

    q = deque(viruses)

    while q:
        value, time, a, b = q.popleft()
        if time == s:
            break
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if na >=0 and na < n and nb >= 0 and nb < n and data[na][nb] == 0:
                data[na][nb] = value
                q.append([value, time+1, na, nb])

# 바이러스 위치
for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            viruses.append([data[i][j], 0, i, j])

viruses.sort()

bfs()
print(data[x-1][y-1])
