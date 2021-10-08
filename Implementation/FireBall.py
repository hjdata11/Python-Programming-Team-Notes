
# https://www.acmicpc.net/problem/20056

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
fire_balls = []

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    data[r-1][c-1].append([r, c, m, s, d])
    fire_balls.append([r, c, m, s, d])

# 파이어볼 이동
def move_fireballs(fire_balls):

    for fire_ball in fire_balls:
        r, c, m, s, d = fire_ball
        nr = (r + s * dx[d]) % n
        nc = (c + s * dy[d]) % n
        data[nr - 1][nc - 1].append([nr, nc, m, s, d])
        data[r - 1][c - 1].remove([r, c, m, s, d])

# 파이어볼 Progress
def progress_fireballs():

    for i in range(n):
        for j in range(n):
            if len(data[i][j]) > 1:
                m, s, d = 0, 0, []
                for v in data[i][j]:
                    m += v[2]
                    s += v[3]
                    d.append(v[4]%2)
                m = m // 5
                if m == 0:
                    data[i][j] = []
                else:
                    s = s // len(data[i][j])
                    if d == [0]*len(data[i][j]) or d == [1]*len(data[i][j]):
                        data[i][j] = [[i+1,j+1,m,s,0],[i+1,j+1,m,s,2],[i+1,j+1,m,s,4],[i+1,j+1,m,s,6]]
                    else:
                        data[i][j] = [[i+1,j+1,m,s,1],[i+1,j+1,m,s,3],[i+1,j+1,m,s,5],[i+1,j+1,m,s,7]]

    fire_balls = []
    for i in range(n):
        for j in range(n):
            if data[i][j] != []:
                fire_balls.extend(data[i][j])
    return fire_balls

# k번 명령
for _ in range(k):
    move_fireballs(fire_balls)
    fire_balls = progress_fireballs()

result = 0
for r, c, m, s, d in fire_balls:
    result += m

print(result)
