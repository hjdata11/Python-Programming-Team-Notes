
# 플로이드 워셜 알고리즘 : 모든 노드에서 다른 모든 노드까지의 최단 경로 계산 (O(N3))
# 거쳐가는 노드를 기준으로 알고리즘을 수행하되 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정이 필요하지 않음.
# 노드의 개수가 적은 상황에서 효과적임
# 점화식 : Dab = min(Dab, Dak + Dkb) : 특정한 노드 k를 거쳐 가는 경우를 확인


INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

# 간선에 대한 정보 입력 받기
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for a in range(1, n+1):
  for b in range(1, n+1):
    if graph[a][b] == INF:
      print("INFINITY", end=" ")
    else:
      print(graph[a][b], end=" ")
  print()