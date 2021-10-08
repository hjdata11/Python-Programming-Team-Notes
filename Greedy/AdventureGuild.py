 
#모험가 길드 : 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정

n = 5
guild = [2, 3, 1, 2, 2]

guild.sort()
result = 0
count = 0
for v in guild:
  count += 1
  if count >= v: #현재 그룹에 포함된 모험가 수가 공포도 이상이면
    result += 1
    count = 0

print(result)
