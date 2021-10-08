
# https://www.acmicpc.net/problem/19236

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from copy import deepcopy

data = [ [None]*4 for _ in range(4) ]
result = 0

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        data[i][j] = [tmp[j*2], tmp[j*2+1]-1]

def rotate(direction):
    return (direction + 1) % 8

def find_fish(tmp_data, v):
    for i in range(4):
        for j in range(4):
            if tmp_data[i][j][0] == v:
                return [i, j]
    return None

def move_fish(tmp_data, now_x, now_y):

    for v in range(1, 17):
        position = find_fish(tmp_data, v)
        if position != None:
            x, y = position[0], position[1]
            direction = tmp_data[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx >= 0 and ny >= 0 and nx < 4 and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        tmp_data[x][y][1] = direction
                        tmp_data[x][y], tmp_data[nx][ny] = tmp_data[nx][ny], tmp_data[x][y]
                        break
                direction = rotate(direction)

def move_shark(tmp_data, now_x, now_y):

    positions = []
    direction = tmp_data[now_x][now_y][1]
    for _ in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if now_x >= 0 and now_y >= 0 and now_x < 4 and now_y < 4:
            if tmp_data[now_x][now_y][0] != -1:
                positions.append([now_x, now_y])
    return positions

def dfs(data, now_x, now_y, total):
    global result
    tmp_data = deepcopy(data)

    total += tmp_data[now_x][now_y][0]
    tmp_data[now_x][now_y][0] = -1

    move_fish(tmp_data, now_x, now_y)

    positions = move_shark(tmp_data, now_x, now_y)
    if len(positions) == 0:
        result = max(result, total)
        return

    for position in positions:
        dfs(tmp_data, position[0], position[1], total)

dfs(data, 0, 0, 0)
print(result)