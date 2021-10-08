# 두 배열의 원소 교체

N = 5
K = 3

A = [1, 2, 5, 4, 3]
B = [5, 5, 6, 6, 5]

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))
