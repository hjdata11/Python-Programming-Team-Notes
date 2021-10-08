
# 병사 배치하기 (가장 긴 증가하는 부분 수열(Longest Increasing Subsequence. LIS))
# 점화식 : 모든 0 <= j < i 에 대하여, D[i] = max(D[i], D[j]+1) if array[j] < array[i]
# https://www.acmicpc.net/problem/18353

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

n = int(input())
List = list(map(int, input().split()))
dp = [1 for i in range(n)]

List = List[::-1]

# 가장 긴 증가하는 부분 수열(LIS)
for i in range(n):
    for j in range(i):
        if List[i] > List[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))