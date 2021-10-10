
# https://www.acmicpc.net/problem/3190

import sys
#sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())

board = [[1] * (n + 2) for _ in range(n + 2)]
for i in range(n):
    for j in range(n):
        board[i + 1][j + 1] = 0

for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = 2

l = int(input())
info = []

for _ in range(l):
    t, d = map(str, input().split())
    t = int(t)
    if d == "D":
        info.append([t, 1])
    else:
        info.append([t, -1])


def solve():
    dir = 1
    q = deque()
    x, y = 1, 1
    q.append([x, y])
    board[x][y] = 3
    answer = 0
    index = 0

    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        answer += 1
        # 벽 안에있는 경우, 자기 자신이 아닌 경우
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and board[nx][ny] != 3:
            if board[nx][ny] == 0:
                a, b = q.popleft()
                board[a][b] = 0
            q.append([nx, ny])
            board[nx][ny] = 3
        else:
            break
        x, y = nx, ny

        if index < l and answer == info[index][0]:
            dir += info[index][1]
            dir %= 4
            index += 1

    return answer

print(solve())