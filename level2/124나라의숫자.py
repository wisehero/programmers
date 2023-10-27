def solution(n):
    answer = ''
    while n:
        # 3의 배수가 아닌 경우
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n//3 - 1
    return answer[::-1]


