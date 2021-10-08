
#문자열 재정렬 : 구현

## 정답 코드
data = input()
result = []
value = 0

for x in data:
  if x.isalpha():
    result.append(x)
  else:
    value += int(x)
  
result.sort()

if value != 0:
  result.append(str(value))

print(''.join(result))

# 체크 포인트 :
# 1. 알파벳을 확인해 주는 라이브러리 isalpha()
# 2. 값이 0이 아닌지 확인

## 나의 코드
String = 'AJKDLSI412K4JSJ9D'

s_List = list(String)
s_List.sort()
Sum = 0

for idex, value in enumerate(s_List):
  if ord(value) < ord('A'):
    Sum += int(value)
  else :
    tmp_List = s_List[idex:]
    break

if Sum != 0:
  result = "".join(tmp_List) + str(Sum)
else:
  result = "".join(tmp_List)

print(result)