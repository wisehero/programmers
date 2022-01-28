def solution(s):
    sum = 0
    answer = ''
    for i in s:
        if i == "(":
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False

    if sum == 0:
        return True
    elif sum > 0:
        return False
