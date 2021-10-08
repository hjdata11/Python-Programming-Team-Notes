
# 크루스칼 알고리즘(최소신장트리) : 그래프에서 모든 노드를 포함하면서 사이클이 존재하지 않은 부분 그래프(ElogE))
# 1. 간선 데이터를 비용에 따라 오름 차순으로 정렬
# 2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인
# 1) 사이클이 발생하지 않은 경우 최소 신장 트리에 포함하면서
# 2) 사이클이 발생하는 경우 최소 신장 트링 포함 X
# 3. 모든 간선에 대하여 2번 과정을 반복

# 특정 원소가 속한 집합을 찾기
def find_parent (parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

#노드의 개수와 간선의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

#모든 간선에 대한 정보 입력 받기
for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 하나씩 간선을 확인하면서
for edge in edges:
  cost, a, b = edge
  # 사이클이 발생하지 않을 경우에만 집합에 포함
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost

print(result)

