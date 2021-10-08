
# 에라토스테네스의 체 (다수의 자연수에 대하여 소수 여부 판별)(O(NloglognN))
# 1. 2부터 N까지의 모든 자연수를 나열
# 2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾음
# 3. 남은 수 중에서 i의 배수를 모두 제거
# 4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복

import math

n = 1000 # 2부터 1000까지의 모든 수에 대하여 소수 판별

array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n)) + 1):
  if array[i] == True:
    j = 2
    while i * j <= n:
      array[i * j] = False
      j += 1

for i in range(2, n+1):
  if array[i]:
    print(i, end=' ')