#https://www.acmicpc.net/problem/13460

# BFS : 한 방향으로 계속 움직이기

import sys
# sys.stdin=open("input.txt","r")
input=sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

m, n = map(int, input().split())
board = []
for _ in range(m):
    board.append(list(map(str, input().strip())))

def move(rx, ry, i, c):
    while board[rx + dx[i]][ry + dy[i]] != "#" and board[rx][ry] != "O":
        rx += dx[i]
        ry += dy[i]
        c += 1
    return rx, ry, c

def bfs(rx, ry, bx, by):

    q = deque()
    q.append([rx, ry, bx, by, 0])
    visited = [[[[False] * n for _ in range(m)] for _ in range(n)] for _ in range(m)]

    while q:
        rx, ry, bx, by, cnt = q.popleft()
        if cnt >= 10:
            continue
        for i in range(4):
            nrx, nry, nrc = move(rx, ry, i, 0)
            nbx, nby, nbc = move(bx, by, i, 0)
            if board[nbx][nby] == "O":
                continue
            elif board[nrx][nry] == "O":
                print(cnt + 1)
                return
            if nrx == nbx and nry == nby:
                if nrc > nbc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append([nrx, nry, nbx, nby, cnt + 1])

    print(-1)

for i in range(m):
    for j in range(n):
        if board[i][j] == "R":
            rx, ry = i, j
        elif board[i][j] == "B":
            bx, by = i, j

bfs(rx, ry, bx, by)
