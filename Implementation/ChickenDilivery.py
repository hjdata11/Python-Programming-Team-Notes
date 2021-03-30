
# https://www.acmicpc.net/problem/15686

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
data = [ list(map(int, input().split())) for _ in range(n) ]

chickens = []
homes = []

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            chickens.append([i, j])
        if data[i][j] == 1:
            homes.append([i, j])

def get_sum(candidate):
    S = 0
    for xh, yh in homes:
        temp = 1e9
        for xc, yc in candidate:
            temp = min(temp, abs(xh-xc)+abs(yh-yc))
        S += temp
    return S

candidates = list(combinations(chickens, m))

mindistance = 1e9
for candidate in candidates:
    mindistance = min(mindistance, get_sum(candidate))

print(mindistance)