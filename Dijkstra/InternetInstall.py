
# https://www.acmicpc.net/problem/1800
# 다이젝스트라, 이분 탐색

import sys
#sys.stdin=open("input.txt","r")
input=sys.stdin.readline
import heapq

n, p, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(p):
    src, dst, cost = map(int, input().split())
    graph[src].append([cost, dst])
    graph[dst].append([cost, src])

def dijkstra(start, limit):
    q = []
    distance = [1e9] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, index = heapq.heappop(q)
        if distance[index] < cost:
            continue
        for i in graph[index]:
            if i[0] > limit:
                if cost + 1 < distance[i[1]]:
                    distance[i[1]] = cost + 1
                    heapq.heappush(q, (cost+1, i[1]))
            else:
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q, (cost, i[1]))

    # 정한 가격 보다 큰 cost의 개수가 k보다 많으면 False
    if distance[n] > k:
        return False
    else:
        return True

start, end = 0, 1000001
answer = 1e9
while start <= end:
    mid = (start + end) // 2
    if dijkstra(1, mid):
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

if answer == 1e9:
    print(-1)
else:
    print(answer)