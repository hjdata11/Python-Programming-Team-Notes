
# itertools : 순열 조합 
# heapq : 우선순위 큐
# bisect: 이진 탐색
# collections : deque, Counter 등의 자료구조
# math : 팩토리얼, 제곱근, 최대공약수, 삼각합수, pi

# eval() : String의 식의 결과를 반환
result = eval("(3+5)*7")
print(result)

# 순열
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

#조합
from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2))
print(result)

#중복 순열 중복 조합
from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

#Counter 등장 횟수 세기
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(dict(counter))

#최대 공약수와 최소 공배수
import math 
def lcm(a, b):
  return a*b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대 공약수
print(lcm(21, 14)) # 최대 공배수