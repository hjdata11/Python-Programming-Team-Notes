
# https://programmers.co.kr/learn/courses/30/lessons/42891

import heapq

def solution(food_times, k):
    
    q = []
    for i, food_time in enumerate(food_times):
        heapq.heappush(q, (food_time, i+1))
    
    small_food = q[0][0]
    prev_food = 0
    
    # k초 후에 몇 번 음식 섭취
    while k - ((small_food-prev_food) * len(q)) >= 0:
        k -= (small_food-prev_food) * len(q)
        prev_food, index = heapq.heappop(q)
        # 섭취해야할 음식이 없을 때 -1 반환
        if not q:
            return -1
        small_food = q[0][0]
    
    # 다시 번호 대로 정렬
    result = sorted(q, key = lambda x : x[1])
    
    return result[k%len(q)][1]