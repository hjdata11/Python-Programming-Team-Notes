
# 최대 공약수 계산 (유클리드 호제법)
# 재귀 함수 : 스택 프레임 메모리에 쌓이는 것을 방지하기 위해 스택 라이브러리 대신 재귀 함수를 이용하는 경우가 많음

def gcd(a, b):
  if a % b == 0:
    return b
  else:
    return gcd(b, a % b)

print(gcd(192, 162))

