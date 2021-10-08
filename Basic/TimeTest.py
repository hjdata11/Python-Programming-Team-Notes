import time
start_time = time.time() #측정 시작

array = [3, 5, 1, 2, 4]

for i in array:
  for j in array:
    temp = i * j

end_time = time.time() #측정 종료
print("time:", end_time-start_time)
  