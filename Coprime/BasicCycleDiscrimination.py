
# 서로소 집합을 활용한 사이클 판별
# 사이클 판별 알고리즘 : 
# 1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인
# 1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행
# 2) 루트 노드가 서로 같다면 사이클이 발생한 것
# 2. 그래프 포함되어 있는 모든 간선에 대하여 1번 과정을 반복

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

cycle = False

for i in range(e):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break

  else:
    union_parent(parent, a, b)

if cycle:
  print("사이클이 발생")
else:
  print("사이클이 발생하지 않음")
