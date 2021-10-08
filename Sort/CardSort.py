
# www.acmicpc.net/problem/1715

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
for i in range(n):
    heapq.heappush(heap, int(input()))

result = 0

# 가장 작은 것을 먼저 더하기
while len(heap) > 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    S = one + two
    result += S
    heapq.heappush(heap, S)

print(result)