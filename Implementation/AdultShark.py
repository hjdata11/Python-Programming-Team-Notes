
# https://www.acmicpc.net/problem/19237


import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]
directions = list(map(int, input().split()))

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

smells = [[[0, 0]] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 냄새 업데이트
def update_smell():

    for i in range(n):
        for j in range(n):
            # 먼저 감소
            if smells[i][j][1] > 0:
                smells[i][j][1] -= 1
            # 새로운 것 삽입
            if data[i][j] != 0:
                smells[i][j] = [data[i][j], k]

# 상어 이동
def move_sharks():
    tmp_data = [[0] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if data[x][y] != 0:
                direction = directions[data[x][y]-1]
                check_move = False
                # 먼저 냄새가 없는 칸 이동
                for index in range(4):
                    nx = x + dx[priorities[data[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[data[x][y]-1][direction-1][index]-1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        # 냄새가 없는지 확인
                        if smells[nx][ny][1] == 0:
                            # 상어 방향 업데이트
                            directions[data[x][y]-1] = priorities[data[x][y]-1][direction-1][index]
                            if tmp_data[nx][ny] == 0:
                                tmp_data[nx][ny] = data[x][y]
                            else:
                                tmp_data[nx][ny] = min(tmp_data[nx][ny], data[x][y])
                            check_move = True
                            break
                if check_move:
                    continue
                # 빈칸이 없을 시 자신의 냄새가 있는 칸 이동
                for index in range(4):
                    nx = x + dx[priorities[data[x][y] - 1][direction-1][index] - 1]
                    ny = y + dy[priorities[data[x][y] - 1][direction-1][index] - 1]
                    if nx >= 0 and nx < n and ny >= 0 and ny < n:
                        if smells[nx][ny][0] == data[x][y]:
                            # 상어 방향 업데이트
                            directions[data[x][y] - 1] = priorities[data[x][y] - 1][direction - 1][index]
                            tmp_data[nx][ny] = data[x][y]
                            break
    return tmp_data

# 1번 상어만 남았는지 체크
def check_shark(data):
    for i in range(n):
        for j in range(n):
            if data[i][j] > 1:
                return False
    return True

time = 0

while True:
    # 냄세 업데이트
    update_smell()
    # 상어 이동
    data = move_sharks()
    time += 1

    if check_shark(data):
        print(time)
        break
        
    if time >= 1000:
        print(-1)
        break