
# https://www.acmicpc.net/problem/19238

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque
import heapq

n, m, f = map(int, input().split())
data = [ [1] * (n+2) for _ in range(n+2) ]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        data[i+1][j+1] = tmp[j]

now_x, now_y = map(int, input().split())
passengers = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 각 지도의 거리 측정
def passenger_distance(now_x, now_y):
    distance = [[-1] * (n+2) for _ in range(n+2)]

    q = deque()
    q.append([now_x, now_y, 0])
    distance[now_x][now_y] = 0
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if distance[nx][ny] == -1 and data[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny, d+1])
    return distance

# 가장 짧은 거리의 고객 선택
def find_passenger(distance):
    global f, success
    heap = []
    for i, passenger in enumerate(passengers):
        x_1, y_1, x_2, y_2 = passenger
        heapq.heappush(heap, [distance[x_1][y_1], x_1, y_1, i])

    dist, _, _, index = heapq.heappop(heap)
    if dist == -1:
        success = False
    f -= dist
    return index

# 손님의 목적지까지
def move(passenger):
    global f, passengers, success
    x_1, y_1, x_2, y_2 = passenger
    distance = passenger_distance(x_1, y_1)
    dist = distance[x_2][y_2]
    if dist == -1:
        success = False
    f -= dist
    now_x, now_y = x_2, y_2
    passengers.remove([x_1, y_1, x_2, y_2])
    return dist, now_x, now_y

success = True
for _ in range(m):
    distance=passenger_distance(now_x, now_y)
    index=find_passenger(distance)
    dist, now_x, now_y = move(passengers[index])

    if f < 0:
        success = False
        break
    else:
        f += 2 * dist

if success:
    print(f)
else:
    print(-1)
