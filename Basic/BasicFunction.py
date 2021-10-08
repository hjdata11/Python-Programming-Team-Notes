
#람다 함수 정렬
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

print(sorted(array, key=lambda x: x[1]))
print(sorted(array, key=lambda x: x[1]), reverse=True)

#여러개 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list(map(lambda a, b: a + b, list1, list2))
print(result)

# 함수 바깥에서 선언된 변수 참조
a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)