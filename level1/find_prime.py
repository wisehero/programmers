def solution(n):
    answer = 0
    for i in range(2, n+1):
        if is_prime(i):
            answer += 1
    return answer

def is_prime(n):
    # 모든 수로 다 나누어볼 필요가 없다.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
