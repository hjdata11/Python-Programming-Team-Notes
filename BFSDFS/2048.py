
# https://www.acmicpc.net/problem/12100

# DFS : 한 방향으로 계속 움직이기 Queue를 이용한 방식

from copy import deepcopy
from collections import deque
n = int(input())
board = [ list(map(int, input().split())) for _ in range(n) ]
answer, q = 0, deque()

def get(i, j):
    if board[i][j]:
        q.append(board[i][j])
        board[i][j] = 0

def merge(i, j, di, dj):
    while q:
        x = q.popleft()
        # 0이라만 그대로
        if not board[i][j]:
            board[i][j] = x
        # 값이 일치하면 2배
        elif board[i][j] == x:
            board[i][j] = x * 2
            i, j = i + di, j + dj
        # 값이 일치하지 않으면 위치이동 후 그대로
        else:
            i, j = i + di, j + dj
            board[i][j] = x

def move(k):
    if k == 0:
        for j in range(n):
            for i in range(n):
                get(i, j)
            merge(0, j, 1, 0)
    elif k == 1:
        for j in range(n):
            for i in range(n-1, -1, -1):
                get(i, j)
            merge(n-1, j, -1, 0)
    elif k == 2:
        for i in range(n):
            for j in range(n):
                get(i, j)
            merge(i, 0, 0, 1)
    elif k == 3:
        for i in range(n):
            for j in range(n-1, -1, -1):
                get(i, j)
            merge(i, n-1, 0, -1)

def dfs(cnt):
    global board, answer
    if cnt == 5:
        for i in range(n):
            answer = max(answer, max(board[i]))
        return
    b = deepcopy(board)

    for k in range(4):
        move(k)
        dfs(cnt + 1)
        board = deepcopy(b)

dfs(0)
print(answer)