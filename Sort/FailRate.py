
# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    result = []
    length = len(stages)
    for i in range(1, N + 1):
        num = stages.count(i)
        if num == 0:
            fail_rate=0
        else:
            fail_rate = num / length
        length -= num
        result.append([i, fail_rate])

    result = sorted(result, key=lambda x: x[1], reverse=True)

    return [x for x, y in result]