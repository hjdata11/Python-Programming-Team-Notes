
# 구현 : 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제

# 상하좌우 문제
# L, R, U, D

n = 5
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x, y = 1, 1

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]

  if nx<1 or ny<1 or nx > n or ny > n:
    continue

  x, y = nx, ny

print(x, y)
