def solution(x):
    answer = True
    # x의 각 자릿수를 더해주기 위해 순서를 가진 자료형으로 바꾼다.
    x = str(x)

    # 각 자릿수의 합
    amount = 0
    for i in x:
        amount += int(i)

    # 각 자릿수의 합으로 x가 나누어지지 않는다면 그것은 하샤드 수가 아니다.
    if int(x) % amount != 0:
        return False

    return answer
