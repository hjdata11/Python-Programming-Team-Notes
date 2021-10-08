
# 순차 탐색 : 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인
# 이진 탐색 : 탐색 범위를 절반씩 좁혀가며 데이터를 탐색 (log2N)

def binary_search1(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2

  if array[mid] == target:
    return mid

  elif array[mid] > target:
    return binary_search1(array, target, start, mid-1)

  else:
    return binary_search1(array, target, mid+1, end)

def binary_search2(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid

    elif array[mid] > target:
      end = mid - 1

    else:
      start = mid + 1
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search1(array, target, 0, n-1)
if result == None:
  print("원소가 존재하지 않습니다.")
else:
  print(result+1)