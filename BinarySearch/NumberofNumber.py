
# 정렬된 배열에서 특정 수의 개수 구하기 (시간복잡도 O(logN))
# 이진 탐색 : 데이터가 정렬되 있기 때문 이진탐색 수행 가능

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0 :
  print(-1)

else:
  print(count)
