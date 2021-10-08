
# 

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
out_sand = 0

# 바람의 방향에 따른 모래 비율
rate_left = [[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]]
rate_down = [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]]
rate_right = [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]]
rate_up = [[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]

# 처음 시작 좌표
x, y = n//2, n//2

# 왼쪽, 아래, 오른, 위
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
length = 1
flag = 0

def spread(rate, nx, ny):

    global out_sand
    a, b = nx-2, ny-2

    tmp = 0
    for i in range(5):
        for j in range(5):
            if rate[i][j] != 'a' and rate[i][j] != 0:
                if -1 < i+a < n and -1 < j+b < n:
                    data[i+a][j+b] += data[nx][ny]*rate[i][j]//100
                else:
                    out_sand += data[nx][ny]*rate[i][j]//100

                tmp += data[nx][ny]*rate[i][j]//100

            elif rate[i][j] == 'a':
                now_x, now_y = i, j

    if -1 < now_x + a < n and -1 < now_y + b < n:
        data[now_x+a][now_y+b] += data[nx][ny] - tmp
    else:
        out_sand += data[nx][ny] - tmp

    data[nx][ny] = 0
    return data


while flag != 1:
    for i in range(4):
        for j in range(length):
            x += dx[i]
            y += dy[i]
            if i == 0:
                spread(rate_left, x, y)
            elif i == 1:
                spread(rate_down, x, y)
            elif i == 2:
                spread(rate_right, x, y)
            elif i == 3:
                spread(rate_up, x, y)

            if x == 0 and y == 0:
                flag = 1
                break

        if i == 1 or i == 3:
            length += 1
        if flag == 1:
            print(out_sand)
            break


