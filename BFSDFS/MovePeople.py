
# www.acmicpc.net/problem/16234

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, l, r = map(int, input().split())
graph = [ list(map(int, input().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 그룹 확인하고 퍼트리기
def process(x, y, index):
    # 연합된 위치들
    united = []
    united.append((x, y))

    q = deque()
    q.append((x, y))
    # 그룹 인덱스
    union[x][y] = index
    # 총 합
    summary = graph[x][y]
    # 숫자
    count = 1

    while q :
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 연합이 안된 경우
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))

    # 연합된 위치 제공 후 각 합을 숫자로 나누기
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0
# 이동 가능한 나라 체크 더이상 이동할 수 없을 때 까지 반복(그룹)
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                # 그룹 인덱스
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

print(total_count)