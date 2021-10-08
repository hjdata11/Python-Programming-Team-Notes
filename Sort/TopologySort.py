
# 위상정렬 : 사이클이 없는 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열 (Direct Acyclic Graph)(O(V+E))
# 1. 진입 차수가 0인 모든 노드를 큐에 넣는다.
# 2. 큐가 빌 때 까지 다음의 과정을 반복
# 1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거
# 2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
# 결과적으로 각 노드가 큐에 들어온 순서가 위상정렬을 수행한 결과와 같음
# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단

from collections import deque

v, e = map(int, input().split())
# 모든 노드의 진입차수는 0으로 초기화
indegree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b) # A에서 B로 이동 가능
  # 진입 차수 1 증가
  indegree[b] += 1

def topology_sort():
  result = []
  q = deque()
  # 진입 차수가 0인 노드를 큐에 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  while q:
    # 큐에서 원소 꺼내기
    now = q.popleft()
    result.append(now)
    for i in graph[now]:
      # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
      indegree[i] -= 1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()