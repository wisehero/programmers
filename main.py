def solution(money):
    answer = []
    a, b = divmod(money,5500)
    answer = [a, b]
    return answer