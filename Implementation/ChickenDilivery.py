
# https://www.acmicpc.net/problem/15686

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]

result = 1e9
house = []
chicken = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house.append([i, j])
        if data[i][j] == 2:
            chicken.append([i, j])

count = 0

# 치킨 거리 계산
def cal_length(chick):
    S = 0
    for h in house:
        tmp = 1e9
        for c in chick:
            tmp = min(tmp, abs(h[0]-c[0])+abs(h[1]-c[1]))
        S += tmp
    return S

# 치킨집 선택
List = list(combinations(chicken, m))
for chick in List:
    length = cal_length(chick)
    result = min(result, length)

print(result)