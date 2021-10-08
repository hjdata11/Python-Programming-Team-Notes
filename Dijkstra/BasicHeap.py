
# 힙(Heap) : 우선순위 큐를 구현하기 위해 사용하는 자료구조 중 하나
# 최소 힙(Min Heap)과 최대 힙(Max Heap)이 있음 (O(logN))

# 최소 힙
import heapq

def heapsort(iterable):
  h = []
  result = []

  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 최대 힙

def heapsort(iterable):
  h = []
  result = []

  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)