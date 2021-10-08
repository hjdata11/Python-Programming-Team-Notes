# 홀수만 포함하는 리스트
array = [i for i in range(20) if i%2 == 1]

print(array)

# 제곱 값을 포함하는 리스트
array = [i * i for i in range(1, 10)]

print(array)

# N * M 2차원 배열 초기화
N = 3
M = 3
array = [[0] * M for _ in range(N)]

print(array)

#리스트에서 특정 값을 가지는 원소를 모두 제거하기
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = [i for i in a if i not in remove_set]
print(result)


a = [4, 3, 2, 1]

#뒤 원소 삽입
a.append(2)

#오름차순 정렬
a.sort()

#내림차순 정렬
a.sort(reverse = True)

#원소 뒤집기
a.reverse()

#특정 인덱스에 데이터 추가
a.insert(2, 3)

#데이터 개수 세기
a.count(3)

#특정 데이터 삭제
a.remove(1)