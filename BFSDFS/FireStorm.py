
# https://www.acmicpc.net/problem/20058

import sys
sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import deque

n, q = map(int, input().split())
w = 2**n
data = [ list(map(int, input().split())) for _ in range(w) ]
Ls = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def rotate(rec):
    tmp = []
    for a in zip(*rec[::-1]):
        tmp.append(a)
    return tmp

def progress(L):
    L = 2**L
    num = w // L

    for i in range(num):
        for j in range(num):
            tmp = []
            for k in range(L):
                tmp.append(data[L*i+k][L*j:L*(j+1)])
            tmp = rotate(tmp)
            for a in range(L):
                for b in range(L):
                    data[L*i+a][L*j+b] = tmp[a][b]

def reduce():

    cnt = [[0]*w for _ in range(w)]

    for x in range(w):
        for y in range(w):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= 0 and nx < w and ny >= 0 and ny < w:
                   if data[nx][ny] > 0:
                       cnt[x][y] += 1

    for x in range(w):
        for y in range(w):
            if data[x][y] > 0 and cnt[x][y] < 3:
                data[x][y] -= 1

for i in range(q):
    progress(Ls[i])
    reduce()

max_num = 0
visited = [[False]*w for _ in range(w)]

def dfs(x, y):

    cnt = 1
    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < w and ny >= 0 and ny < w:
                if not visited[nx][ny] and data[nx][ny] > 0:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

for i in range(w):
    for j in range(w):
        if data[i][j] > 0 and not visited[i][j]:
            cnt = dfs(i, j)
            max_num = max(cnt, max_num)

print(sum([sum(d) for d in data]))
print(max_num)