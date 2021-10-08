
# https://www.acmicpc.net/problem/18352

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1]*(n+1)
distance[x] = 0

# bfs
def bfs(graph, start):

    # 시작 노드 삽입
    q = deque([start])
    while q:
        # 노드 추출
        now = q.popleft()
        # 현재에서 이동 여부 확인
        for node in graph[now]:
            # 방문 여부 확인
            if distance[node] == -1:
                distance[node] = distance[now] + 1
                q.append(node)

    # 거리 측정
    check = False
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
            check = True

    if check == False:
        print(-1)

bfs(graph, x)