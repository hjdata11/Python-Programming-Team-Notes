
# 병사 배치하기 (가장 긴 증가하는 부분 수열(Longest Increasing Subsequence. LIS))
# 점화식 : 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]

n = int(input())
array = list(map(int, input().split()))

array.reverse()

dp = [1] * n

for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))
