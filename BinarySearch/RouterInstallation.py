
# https://www.acmicpc.net/problem/2110

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

n, c = list(map(int, input().split(' ')))
array = []
for _ in range(n):
    x = int(input())
    array.append(x)

array.sort()

start = 1 # 최소 거리
end = array[-1] - array[0] # 최대 거리
result = 0

while(start <= end):
    mid = (start + end) // 2
    value = array[0]
    count = 1
    # 1개씩 고유기 설치
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
        # c개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
    if count >= c:
        start = mid + 1
        result = mid
    else:  # c개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        end = mid - 1

print(result)