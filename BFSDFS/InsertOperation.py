
# https://www.acmicpc.net/problem/14888

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

max_value = -1e9
min_value = 1e9

n = int(input())
List = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

# 모든 연산의 경우의 수 구하기
def dfs(idx, now):
    global min_value, max_value, add, sub, mul, div

    if idx == n:
        min_value = min(now, min_value)
        max_value = max(now, max_value)
        return

    if add > 0:
        add -= 1
        dfs(idx+1, now + List[idx])
        add += 1
    if sub > 0:
        sub -= 1
        dfs(idx+1, now - List[idx])
        sub += 1

    if mul > 0:
        mul -= 1
        dfs(idx+1, now * List[idx])
        mul += 1

    if div > 0:
        div -= 1
        dfs(idx+1, int(now/List[idx]))
        div += 1

dfs(1, List[0])
print(max_value)
print(min_value)