
# 특정한 합을 가지는 부분 연속 수열 찾기
# 합이 M인 부분 연속 수열의 개수
# 1. 시작점과 끝점이 첫 번째 원소의 인덱스 0을 가리키도록 한다.
# 2. 현재 부분 합이 M과 같다면, 카운트 한다.
# 3. 현재 부분 합이 M보다 작다면, end를 1 증가시킨다.
# 4. 현재 부분 합이 M보다 크거나 같다면, start를 1 증가시킨다.
# 5. 모든 경우를 확인할 때까지 2번 부터 4번 까지의 과정을 반복한다.

n = 5
m = 5
data = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(n):
  # end를 가능한 만큼 이동시키기
  while interval_sum < m and end < n:
    interval_sum += data[end]
    end += 1

  if interval_sum == m:
    count += 1
  interval_sum -= data[start]

print(count)