
# 서로소 집합 자료구조 : 합치기 찾기(Union Find) 자료구조

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
  # 루트 노드를 찾을 때까지 재귀 호출
  if parent[x] != x:
    return find_parent(parent, parent[x])
  # 부모 테이블 값을 바로 갱신
  return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')

print

print ('부모 테이블: ', end='')
for i in range(1, v+1):
  print(parent[i], end=' ')
