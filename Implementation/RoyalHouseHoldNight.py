

# 왕실의 나이트 : 구현

## 정답 코드
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
  nx_row = row +step[0]
  nx_column = column +step[1]
  if nx_row >= 1 and nx_row <= 8 and nx_column >= 1 and nx_column <= 8:
    result += 1

print(result)

# 체크 포인트 :
# 1. 숫자 아스키 코든 변환
# 2. 방향의 각 step을 묶음

## 나의 코드
Input = 'a1'

# R, L, U, D
dx = [-1, 1, -2, 2, -1, 1, -2, 2]
dy = [2, 2, 1, 1, -2, -2, -1, -1]

tmp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

x = tmp.index(Input[0]) + 1
y = int(Input[1])
count = 0

for i in range(len(dx)):
  nx = x + dx[i]
  ny = y + dy[i]

  if nx <= 0 or ny <= 0 or nx > 8 or ny > 8 :
    continue
  count += 1

print(count)
