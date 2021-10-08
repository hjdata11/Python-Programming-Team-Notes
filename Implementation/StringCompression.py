
# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    result = 1000

    if len(s) == 1:
        return 1

    # 문자 길이에 따른 압축
    for length in range(1, len(s) // 2 + 1):
        count = 1
        # 이전 문자
        tmp = ''
        # 길이에 따라 문자 자르기 (마지막 숫자 붙이기)
        for i in range(0, len(s) + 1, length):
            # 같은 경우 숫자 세기
            if s[i:i + length] == tmp[-length:]:
                count += 1
            # 아닌 경우 문자 붙이기
            else:
                if count >= 2:
                    tmp += str(count)
                tmp += s[i:i + length]
                count = 1

        print(len(tmp))
        result = min(result, len(tmp))

    return result