
# 큐는 시간 복잡도상 deque 이용

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
