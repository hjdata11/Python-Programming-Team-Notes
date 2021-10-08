

#곱하기 혹은 더하기 : 두 수에 대하여 연산을 수행할 때, 두 수중 에서 하나라도 1 이하인 경우에는 더하며, 두수가 모두 2 이상인 경우에는 곱하면 정답

data = input()

result = int(data[0])
for i in range(1, len(data)):
  num = int(data[i])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)
