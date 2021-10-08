
# input() 한 줄의 문자열을 입력 받는 함수
# map() 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용
# rstrip() 줄 바꿈

#빠르게 입력 받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

#데이터 개수 입력
n = int(input())

#공백 기준으로 구분된 데이터 입력
list(map(int, input().split()))

#공백 기준으로 데이터가 많이 않다면
a, b, c = map(int, input().split())

#줄 바꿈 안되게 end 사용
print(7, end=" ")
print(8, end=" ")

#f-string 예제
answer = 7
print(f"정답은 {answer}입니다.")

number = 2.341
print(f'{number:.2f}')