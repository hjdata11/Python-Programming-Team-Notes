
# https://www.acmicpc.net/problem/20055

import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
duration = deque()
belt = deque()
duration.extend(list(map(int, input().split())))
belt.extend([0] * n)

# 벨트 이동
def move_belt():
    global belt
    global duration

    # 벨트 한칸 회전
    belt.rotate(1)
    duration.rotate(1)
    belt[-1] = 0

    # 가장 먼저 벨트에 올라간 로봇 부터 이동
    for i in range(-2, -n-1, -1):
        if belt[i] == 1 and belt[i+1] == 0 and duration[i+1-n] > 0:
            belt[i] = 0
            belt[i+1] = 1
            duration[i+1-n] -= 1
    belt[-1] = 0

    # 올라가는 위치에 로봇이 없으면 올림
    if belt[0] == 0 and duration[0] > 0:
        belt[0] = 1
        duration[0] -= 1

# 내구도 체크
def check_durability():
    num = duration.count(0)
    if num >= k:
        return True
    return False

level = 1
while True:
    move_belt()
    if check_durability():
        print(level)
        break
    level += 1