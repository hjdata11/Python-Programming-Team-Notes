# 볼링골 고르기

n, m = 5, 3
values = [1, 3, 2, 3, 2]

array = [0] * 11

# 각 공의 무게 개수
for v in values:
    array[v] += 1

result = 0
for i in range(1, m + 1):
    n -= array[i]  # 자기 자신을 선택할 수 있는 수 제외
    result += array[i] * n  # 선택하는 경우의 수 곱하기

print(result)
