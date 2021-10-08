a = {
  '홍길동' : 97,
  '이순신' : 98
}

#list형 변환
key_list = list(a.keys())
print(key_list)

#집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

#집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

#새로운 원소 추가
data.add(4)
print(data)

#원소 여러개 추가
data.update([5, 6])
print(data)

#특정 값을 갖는 원소 삭제
data.remove(3)
print(data)

a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

#합집합
print(a | b)

#교집합
print(a & b)

#차집합
print(a - b)