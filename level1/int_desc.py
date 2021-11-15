def solution(n):
    answer = 0
    answer = list(str(n))
    answer.sort(reverse=True)
    # 문자열.join()을 기억하자....
    return int(''.join(answer))
