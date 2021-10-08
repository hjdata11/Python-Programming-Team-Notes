
# https://www.acmicpc.net/problem/14501

import sys
#sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
t = []
p = []
max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 최대 값을 dp에 계속 갱신
for i in range(n-1, -1, -1):
    time = t[i] + i

    # 기간 안에 끝나는 경우
    if time <= n:
        dp[i] = max(max_value, p[i]+dp[time])
        max_value = dp[i]
    # 긴간 안에 못 끝나는 경우
    else:
        dp[i] = max_value

print(max_value)