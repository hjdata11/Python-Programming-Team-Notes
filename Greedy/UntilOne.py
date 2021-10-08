# 1이 될 때 까지 : 최대한 많이 나누는 작업

#n, k = map(int, input().split())
n = 17
k = 4
result = 0

while True:
  target = (n//k) * k
  result += (n - target)
  n = target
  if n < k:
    break

  result += 1
  n //= k

result += (n - 1)

print(result)
