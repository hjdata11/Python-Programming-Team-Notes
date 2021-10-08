
# https://www.acmicpc.net/problem/18352

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import defaultdict, deque


n, m, k, x = map(int, input().split())
dict = defaultdict(list)
distance = [-1]*(n+1)
distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dict[a].append(b)

def bfs(start):

    q = deque([start])

    while q:
        v = q.popleft()
        for nv in dict[v]:
            if distance[nv] == -1:
                distance[nv] = distance[v] + 1
                q.append(nv)

    # 출력
    flag = True
    for i, d in enumerate(distance):
        if d == k:
            print(i)
            flag = False

    if flag:
        print(-1)


bfs(x)

