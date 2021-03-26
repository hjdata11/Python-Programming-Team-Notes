import heapq

def solution(food_times, k):
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
        
    small_food = q[0][0]
    prev_food = 0
    
    # 완판을 완주 할 수 있는 경우
    while k - ((small_food - prev_food) * len(q)) >= 0:
        k -= (small_food - prev_food) * len(q)
        prev_food, index = heapq.heappop(q)
        if not q:
            return -1
        small_food = q[0][0]
    
    result = sorted(q, key=lambda x: x[1])
    return result[k % len(q)][1]