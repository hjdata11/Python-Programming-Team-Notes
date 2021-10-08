
# 다익스트라 최단 경로 알고리즘 : 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로
# 매 상황에서 가장 비용이 적은 노드를 선택 (그리디)

# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신
# 5. 위 과정에서 3번과 4번을 반복

# 한번 처리된 노드의 최단 거리는 고정
# O(V2)

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n+1)]
visited = [[False] * (n+1)]
distance = [INF] * (n+1)

# 모든 간선 정보를 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_value and not visited[i]:
      min_value = distance[i]
      index = i
  return index


def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  # 출발 노드로 부터 도달이 가능한 거리들을 갱신
  for j in graph[start]:
    distance[j[0]] = j[1]

  for i in range(n-1):
    # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
    now = get_smallest_node()
    visited[now] = True
    # 현재 노드와 연결된 다른 노드를 확인
    for j in graph[now]:
      cost = distance[now] + j[1]

      if cost < distance[j[0]]:
        distance[j[0]] = cost
    
dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    print("INFINTY")
  else:
    print(distance[i])
