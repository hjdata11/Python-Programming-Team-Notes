
# https://www.acmicpc.net/problem/19237

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

array = [ list(map(int, input().split())) for _ in range(n) ]
directions = list(map(int, input().split()))

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

# [상어 번호, 남은 시간]
smell = [[[0,0]] * n  for _ in range(n)]

def update_smell():

    for i in range(n):
        for j in range(n):

            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move_sharks():

    new_array = [[0]*n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if array[x][y] != 0:
                direction = directions[array[x][y]-1]
                check_move = False
                # 냄새가 존재하는지 확인
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:

                            # 상어 방향 업데이트
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]

                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])

                            check_move = True
                            break

                if check_move:
                    continue

                # 주변에 냄새가 남아 있다면 자신의 내세로 이동
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]:
                            # 상어 방향 업데이트
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny] = array[x][y]
                            break

    return new_array

time = 0
while True:
    # 냄세 업데이트
    update_smell()
    # 상어 이동 업데이트
    array = move_sharks()

    time += 1

    #1번 상어 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
