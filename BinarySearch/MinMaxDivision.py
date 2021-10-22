# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def isValid(A, max_block_cnt, max_block_size):
    block_sum = 0
    block_cnt = 0

    for a in A:
        if block_sum + a > max_block_size:
            block_sum = a
            block_cnt += 1
        else:
            block_sum += a
        if block_cnt >= max_block_cnt:
            return False
    return True

def solution(K, M, A):
    # write your code in Python 3.6
    max_block_cnt = K
    start = max(A)
    end = sum(A)

    if max_block_cnt == 1:
        return end
    if max_block_cnt >= len(A):
        return start

    while (start <= end):
        mid = (start + end) // 2
        if isValid(A, max_block_cnt, mid):
            end = mid - 1
        else:
            start = mid + 1

    return start