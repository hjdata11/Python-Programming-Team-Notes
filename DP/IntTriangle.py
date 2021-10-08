
# https://www.acmicpc.net/problem/1932

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up = 0
        else:
            left_up = data[i-1][j-1]

        if j == i:
            up = 0
        else:
            up = data[i-1][j]

        data[i][j] = data[i][j] + max(left_up, up)

print(max(data[n-1]))
