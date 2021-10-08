
# 파라메트릭 서치 : 최적화 문제를 결정 문제 (예 혹은 아니오)로 바꾸어 해결하는 기법
# 이진 탐색 : 큰 탐색 범위 에서 조건의 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좀혀서 해결

def add_Duck(arr, mid):
  S = 0
  for val in arr:
    if val > mid:
      S += (val - mid)
  
  return S

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    total = add_Duck(arr, mid)

    # 떡의 양이 적은 경우 더 많이 자르기 (왼쪽 부분) : 떡의 양이 적으면 안됨으로 우선 조건
    if total < target:
      end = mid - 1

    # 떡의 양이 많은 경우 덜 자르기 (오른쪽 부분)
    else :
      result = mid
      start = mid + 1

  return result
    

N = 4
M = 6
arr = [19, 15, 10, 17]

result = binary_search(arr, M, 0, max(arr))

print(result)
